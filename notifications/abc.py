from abc import ABC, abstractmethod


class NotificationABC(ABC):
    """
    Abstract class representing a generic notification manager.
    Classes inheriting from this must implement the send method.
    """
    @abstractmethod
    def send(self, owner: str, message: str, ) -> None:
        pass