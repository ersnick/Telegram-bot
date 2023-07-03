import json
import logging

import pika
from models.notification import Notification
from pika.adapters.blocking_connection import BlockingChannel
from pika.exchange_type import ExchangeType
from pika.spec import Basic, BasicProperties
from service import notification_service as service

logger = logging.getLogger()

QUEUE = 'send-notification'
EXCHANGE = 'service.notification'
ROUTING_KEY = 'notification-routing-key'


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
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
    channel.exchange_declare(exchange=EXCHANGE, exchange_type=ExchangeType.topic.name)

    channel.queue_declare(queue=QUEUE, durable=True)
    channel.queue_bind(queue=QUEUE,
                       exchange=EXCHANGE,
                       routing_key=ROUTING_KEY)
    channel.basic_consume(queue=QUEUE, auto_ack=True, on_message_callback=callback)

    logger.info('RabbitMQ starts')

    channel.start_consuming()
