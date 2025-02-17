"""
Description: This file contains the Client class for the banking application.
Author: Md Apurba Khan
"""

from email_validator import EmailNotValidError, validate_email


class Client:
    """
    Represents a client with unique identification and contact details.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new client with a client number, first name, last name, and email address.

        Raises:
            ValueError: If client_number is not an integer.
            ValueError: If first_name or last_name is blank after stripping.
        """
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")

        first_name = first_name.strip()
        last_name = last_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        if not last_name:
            raise ValueError("Last name cannot be blank.")

        try:
            validated_email = validate_email(email_address, check_deliverability=False).normalized
        except EmailNotValidError:
            validated_email = "email@pixell-river.com"

        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = validated_email

    @property
    def client_number(self) -> int:
        """Returns the client number."""
        return self.__client_number

    @property
    def first_name(self) -> str:
        """Returns the first name."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Returns the last name."""
        return self.__last_name

    @property
    def email_address(self) -> str:
        """Returns the email address."""
        return self.__email_address

    def __eq__(self, other) -> bool:
        """Check if two clients are equal based on client number."""
        return isinstance(other, Client) and self.__client_number == other.client_number

    def __lt__(self, other) -> bool:
        """Check if this client is less than another client based on client number."""
        return isinstance(other, Client) and self.__client_number < other.client_number

    def __gt__(self, other) -> bool:
        """Check if this client is greater than another client based on client number."""
        return isinstance(other, Client) and self.__client_number > other.client_number

    def __str__(self) -> str:
        """Returns a formatted string representation of the client."""
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"
