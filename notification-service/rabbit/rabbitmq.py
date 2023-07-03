import json
import logging

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from models.notification import Notification

from service import notification_service as service

logger = logging.getLogger()


def callback_1(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
    json_body = str(body.decode('utf-8'))
    notification = json.loads(json_body, object_hook=lambda n: Notification(user_id=n['user_id'],
                                                                            chat_id=n['chat_id'],
                                                                            text=n['text'],
                                                                            title=n['title'],
                                                                            send_time=n['send_time']))

    service.save_notification(notification=notification)


async def connect_to_broker():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.exchange_declare(exchange='test.py', exchange_type='topic')

    channel.queue_declare(queue='test-queue', durable=False)
    channel.queue_bind(queue='test-queue', exchange='test.py', routing_key='test-routing-key')
    channel.basic_consume(queue='test-queue', auto_ack=True, on_message_callback=callback_1)

    logger.info('RabbitMQ starts')

    channel.start_consuming()
