from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime
import re

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class Client(Observer):
    """Class representing a bank client, acting as an observer."""

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str) -> None:
        """Initialize a client with basic information."""
        if client_number is None:
            raise ValueError("Client number cannot be None.")
        if isinstance(client_number, str):
            if not client_number.strip():
                raise ValueError("Client number cannot be empty.")
            try:
                client_number = int(client_number)
            except ValueError:
                raise ValueError("Client number must be a valid integer or string representation of an integer.")
        elif not isinstance(client_number, int):
            raise ValueError("Client number must be an integer or string representation of an integer.")
        self._client_number = client_number

        if not isinstance(first_name, str) or not first_name.strip() or first_name is None:
            raise ValueError("First name must be a non-empty string.")
        if not isinstance(last_name, str) or not last_name.strip() or last_name is None:
            raise ValueError("Last name must be a non-empty string.")
        
        self._first_name = first_name
        self._last_name = last_name

        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not isinstance(email_address, str) or not email_address.strip() or not email_pattern.match(email_address):
            self._email_address = "email@pixell-river.com"
        else:
            self._email_address = email_address

    @property
    def client_number(self) -> int:
        """Get the client number."""
        return self._client_number

    @property
    def first_name(self) -> str:
        """Get the first name."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """Get the last name."""
        return self._last_name

    @property
    def email_address(self) -> str:
        """Get the email address."""
        return self._email_address

    def update(self, message: str) -> None:
        """Update the client with a notification message."""
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        email_message = f"Notification for {self._client_number}: {self._first_name} {self._last_name}: {message}"
        simulate_send_email(self._email_address, subject, email_message)

    def __eq__(self, other: object) -> bool:
        """Check equality based on client number."""
        if not isinstance(other, Client):
            return False
        return self._client_number == other._client_number

    def __lt__(self, other: object) -> bool:
        """Compare clients based on client number for less than."""
        if not isinstance(other, Client):
            return NotImplemented
        return str(self._client_number) < str(other._client_number)

    def __str__(self) -> str:
        """Return a string representation of the Client."""
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}"