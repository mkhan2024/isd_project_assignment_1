"""
Description: This file contains the Client class for the banking application.
Author: Md Apurba Khan
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(self, client_number, first_name, last_name, email):
        """
        Set up a new Client instance.
        
        Args:
            client_number (int): Client's unique identifier
            first_name (str): Client's first name
            last_name (str): Client's last name
            email (str): Client's email address
        
        Raises:
            ValueError: For invalid client number or empty names
        """
        if not isinstance(client_number, int) or client_number < 1000:
            raise ValueError("Client number must be an integer of at least 1000")
        self._client_number = client_number

        if not first_name.strip():
            raise ValueError("First name can't be empty")
        self._first_name = first_name.strip()

        if not last_name.strip():
            raise ValueError("Last name can't be empty")
        self._last_name = last_name.strip()

        try:
            validated_email = validate_email(email)
            self._email = validated_email.email
        except EmailNotValidError:
            self._email = "email@pixell-river.com"

    @property
    def client_number(self):
        return self._client_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    def __str__(self):
        return f"{self._last_name}, {self._first_name} [{self._client_number}] - {self._email}"

    def __repr__(self):
        return f"Client({self._client_number}, {self._first_name}, {self._last_name}, {self._email})"

    def __eq__(self, other):
        return self._client_number == other._client_number

    def __hash__(self):
        return hash(self._client_number)

    def __lt__(self, other):
        return self._client_number < other._client_number   

    def __gt__(self, other):
        return self._client_number > other._client_number   