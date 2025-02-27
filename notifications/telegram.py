from typing import Optional

import urllib.request
import urllib.parse

from notifications.abc import NotificationABC


class TelegramNotification(NotificationABC):
    """
    Telegram notification manager
    """
    def __init__(self, token: str, chat_id: str, thread_id: Optional[str] = None):
        self.url = f"https://api.telegram.org/bot{token}/sendMessage"
        self.chat_id = chat_id
        self.thread_id = thread_id

    def send(self, owner: str, message: str) -> None:
        params = urllib.parse.urlencode({
            "chat_id": self.chat_id,
            "message_thread_id": self.thread_id,
            "text": f"{owner}: {message}"
        })

        urllib.request.urlopen(f"{self.url}?{params}")
