from abc import ABC

__author__ = "Your Full Name"
__version__ = "1.3.0"

class Subject(ABC):
    """Abstract base class for subjects in the Observer Pattern.

    Attributes:
        _observers (list): The list of observers attached to the subject.
    """

    def __init__(self):
        """Initialize the subject with an empty list of observers."""
        self._observers = []

    def attach(self, observer):
        """Attach an observer to the subject.

        Args:
            observer (Observer): The observer to be added.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Detach an observer from the subject.

        Args:
            observer (Observer): The observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        """Notify all observers of a state change.

        Args:
            message (str): The message to be sent to all observers.
        """
        for observer in self._observers:
            observer.update(message)