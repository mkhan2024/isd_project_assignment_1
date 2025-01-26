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
        self.client = Client(1001, "John", "Doe", "jdoe@example.com")

    def test_init(self):
        self.assertEqual(self.client.client_number, 1001)
        self.assertEqual(self.client.first_name, "John")
        self.assertEqual(self.client.last_name, "Doe")
        self.assertEqual(self.client.email, "jdoe@example.com")

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            Client("invalid", "John", "Doe", "jdoe@example.com")
        with self.assertRaises(ValueError):
            Client(999, "John", "Doe", "jdoe@example.com")  # Test for number less than 1000

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Client(1001, "", "Doe", "jdoe@example.com")

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Client(1001, "John", "", "jdoe@example.com")

    def test_invalid_email(self):
        client = Client(1001, "John", "Doe", "invalid")
        self.assertEqual(client.email, "email@pixell-river.com")

    def test_empty_email(self):
        client = Client(1001, "John", "Doe", "")
        self.assertEqual(client.email, "email@pixell-river.com")

    def test_str(self):
        expected = "Doe, John [1001] - jdoe@example.com"
        self.assertEqual(str(self.client), expected)

if __name__ == '__main__':
    unittest.main()