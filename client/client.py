from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime
import re

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class Client(Observer):
    """Class representing a bank client, acting as an observer.

    Attributes:
        _client_number: The unique client number (int or str).
        _first_name (str): The client's first name.
        _last_name (str): The client's last name.
        _email_address (str): The client's email address.
    """

    def __init__(self, client_number, first_name, last_name, email_address):
        """Initialize a client with basic information.

        Args:
            client_number: The unique client number (int or str representing an integer).
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Raises:
            ValueError: If client_number is not a valid integer (or string representation), or if first_name, last_name are invalid.
        """
        # Validate client_number
        if client_number is None:
            raise ValueError("Client number cannot be None.")
        if isinstance(client_number, str):
            if not client_number.strip():
                raise ValueError("Client number cannot be empty.")
            try:
                int(client_number)  # Ensure it’s a valid integer string
            except ValueError:
                raise ValueError("Client number must be a valid integer or string representation of an integer.")
        elif not isinstance(client_number, int):
            raise ValueError("Client number must be an integer or string representation of an integer.")
        self._client_number = client_number  # Keep as provided (int or str)

        # Validate first_name and last_name
        if not isinstance(first_name, str) or not first_name.strip() or first_name is None:
            raise ValueError("First name must be a non-empty string.")
        if not isinstance(last_name, str) or not last_name.strip() or last_name is None:
            raise ValueError("Last name must be a non-empty string.")
        
        self._first_name = first_name
        self._last_name = last_name

        # Validate email_address
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not isinstance(email_address, str) or not email_address.strip() or email_address is None or not email_pattern.match(email_address):
            self._email_address = "email@pixell-river.com"  # Default for invalid email
        else:
            self._email_address = email_address

    @property
    def client_number(self):
        """Get the client number.

        Returns:
            The client number (int or str).
        """
        return self._client_number

    @property
    def first_name(self):
        """Get the first name.

        Returns:
            str: The first name.
        """
        return self._first_name

    @property
    def last_name(self):
        """Get the last name.

        Returns:
            str: The last name.
        """
        return self._last_name

    @property
    def email_address(self):
        """Get the email address.

        Returns:
            str: The email address.
        """
        return self._email_address

    def update(self, message):
        """Update the client with a notification message.

        Simulates sending an email by writing to observer_emails.txt.

        Args:
            message (str): The message to be processed.
        """
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        email_message = f"Notification for {self._client_number}: {self._first_name} {self._last_name}: {message}"
        simulate_send_email(subject, email_message)

    def __eq__(self, other):
        """Check equality based on client number.

        Args:
            other (Client): The client to compare with.

        Returns:
            bool: True if client numbers match, False otherwise.
        """
        if not isinstance(other, Client):
            return False
        return self._client_number == other._client_number

    def __lt__(self, other):
        """Compare clients based on client number for less than.

        Args:
            other (Client): The client to compare with.

        Returns:
            bool: True if this client number is less than the other, False otherwise.
        """
        if not isinstance(other, Client):
            return NotImplemented
        return str(self._client_number) < str(other._client_number)  # Compare as strings for consistency

    def __str__(self):
        """Return a string representation of the Client.

        Returns:
            str: Formatted as 'Last, First [client_number] - email_address'.
        """
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email_address}"