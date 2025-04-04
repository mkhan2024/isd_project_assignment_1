from abc import ABC, abstractmethod

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"

class Observer(ABC):
    """Abstract base class for observers in the Observer Pattern."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Update the observer with a message."""
        pass

class Subject(ABC):
    """Abstract base class for subjects in the Observer Pattern."""

    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        """Add an observer to the list."""
        pass

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        """Remove an observer from the list."""
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """Notify all observers of a change."""
        pass