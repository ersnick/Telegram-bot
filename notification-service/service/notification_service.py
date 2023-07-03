import logging

from models.notification import Notification
from models.notification_db import NotificationDB
from repository import notification_repository as repository
from repository import notification_redis as redis_repository

logger = logging.getLogger()


def check_event_time():
    notifications = redis_repository.get_with_now_send_time_notifications()
    for notification in notifications:
        print(
            f'Send notification to user_id: {notification.user_id}, on chat_id: {notification.chat_id} with title: {notification.title}')
    logger.info('Check sending time nearest events')


def check_event_on_next_hour():
    logger.info('Check events on next hour')
    saved_notifications = repository.get_notification_on_hour()
    saved_notifications.sort(key=lambda x: x.send_time, reverse=False)
    notifications = []
    for notification in saved_notifications:
        notifications.append(Notification(id=notification.id,
                                          user_id=notification.user_id,
                                          chat_id=notification.chat_id,
                                          text=notification.text,
                                          title=notification.title,
                                          send_time=notification.send_time))
    redis_repository.push_event_to_queue(notifications)


def save_notification(notification: Notification) -> None:
    db_model = NotificationDB(user_id=notification.user_id,
                              chat_id=notification.chat_id,
                              text=notification.text,
                              title=notification.title,
                              send_time=notification.send_time)

    repository.save_notification(notification=db_model)
