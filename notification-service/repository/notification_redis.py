import json
from datetime import datetime

import redis
from models.notification import Notification

repository = redis.Redis(host='localhost', port=6379, db=0)


def push_event_to_queue(notifications: list[Notification]) -> None:
    saved = repository.lrange('notifications', start=0, end=-1)
    for notification in notifications:
        n_json = bytes(notification.toJSON().encode('utf-8'))
        if n_json in saved:
            continue
        repository.lpush('notifications', n_json)


def get_with_now_send_time_notifications() -> list[Notification]:
    now = datetime.now()
    notifications = []
    while True:
        json_notification = repository.rpop('notifications')
        if json_notification is None:
            break
        notification = json.loads(json_notification)
        notification_time = datetime.fromtimestamp(notification['send_time'])
        if notification_time.minute == now.minute:
            notifications.append(Notification(id=notification['id'],
                                              user_id=notification['user_id'],
                                              chat_id=notification['chat_id'],
                                              text=notification['text'],
                                              title=notification['title'],
                                              send_time=notification['send_time']))
        else:
            repository.rpush('notifications', json_notification)
            break
    return notifications
