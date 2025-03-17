from abc import ABC, abstractmethod

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"

class Observer(ABC):
    """Abstract base class for observers in the Observer Pattern."""

    @abstractmethod
    def update(self, message):
        """Update the observer with a message.

        Args:
            message (str): The message to be processed by the observer.
        """
        pass