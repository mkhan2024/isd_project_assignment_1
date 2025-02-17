"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute
the following command:
    python -m unittest tests/test_client.py
"""

import unittest

from client.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        """Set up a test client instance."""
        self.client = Client(1001, "John", "Doe", "jdoe@example.com")

    def test_valid_client(self):
        """Test client initialization with valid values."""
        self.assertEqual(self.client.client_number, 1001)
        self.assertEqual(self.client.first_name, "John")
        self.assertEqual(self.client.last_name, "Doe")
        self.assertEqual(self.client.email_address, "jdoe@example.com")

    def test_invalid_client_number(self):
        """Test client creation with invalid client number."""
        with self.assertRaises(ValueError):
            Client("invalid", "John", "Doe", "jdoe@example.com")

    def test_invalid_first_name(self):
        """Test client creation with empty first name."""
        with self.assertRaises(ValueError):
            Client(1001, "", "Doe", "jdoe@example.com")

    def test_invalid_last_name(self):
        """Test client creation with empty last name."""
        with self.assertRaises(ValueError):
            Client(1001, "John", "", "jdoe@example.com")

    def test_invalid_email(self):
        """Test client creation with invalid email format."""
        client = Client(1001, "John", "Doe", "invalid_email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_empty_email(self):
        """Test client creation with empty email, should default."""
        client = Client(1001, "John", "Doe", "")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_str_method(self):
        """Test the __str__ method of the Client class."""
        expected = "Doe, John [1001] - jdoe@example.com"
        self.assertEqual(str(self.client), expected)

    def test_equality(self):
        """Test that two clients with the same client number are equal."""
        client2 = Client(1001, "Jane", "Smith", "janesmith@example.com")
        self.assertEqual(self.client, client2)

    def test_inequality(self):
        """Test that two clients with different client numbers are not equal."""
        client2 = Client(1002, "Jane", "Smith", "janesmith@example.com")
        self.assertNotEqual(self.client, client2)

    def test_comparison(self):
        """Test < and > operators for clients."""
        client2 = Client(1002, "Jane", "Smith", "janesmith@example.com")
        self.assertTrue(self.client < client2)
        self.assertFalse(self.client > client2)


if __name__ == "__main__":
    unittest.main()
