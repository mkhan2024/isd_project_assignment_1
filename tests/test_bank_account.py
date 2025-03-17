import unittest
from datetime import date
from tests.test_utils import TestableBankAccount  # Adjust import path if necessary

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class TestBankAccount(unittest.TestCase):
    """Test case for the BankAccount class."""

    def setUp(self):
        """Set up a testable bank account instance before each test."""
        self.bank_account = TestableBankAccount("2001", "1001", 1000.00, date(2023, 1, 1))

    def test_valid_bank_account(self):
        """Test bank account initialization with valid values."""
        self.assertEqual(self.bank_account.account_number, "2001")
        self.assertEqual(self.bank_account.client_number, "1001")
        self.assertEqual(self.bank_account.balance, 1000.00)
        self.assertEqual(self.bank_account.date_created, date(2023, 1, 1))

    def test_invalid_account_number(self):
        """Test bank account creation with an invalid account number."""
        with self.assertRaises(TypeError):
            TestableBankAccount(None, "1001", 1000.00, date(2023, 1, 1))

    def test_invalid_client_number(self):
        """Test bank account creation with an invalid client number."""
        with self.assertRaises(TypeError):
            TestableBankAccount("2001", None, 1000.00, date(2023, 1, 1))

    def test_invalid_balance(self):
        """Test bank account creation with an invalid balance."""
        bank_account = TestableBankAccount("2001", "1001", "invalid_balance", date(2023, 1, 1))
        self.assertEqual(bank_account.balance, 0.0)  # Should default to 0.0

    def test_deposit_invalid(self):
        """Test deposit of a non-numeric value."""
        with self.assertRaises(ValueError):
            self.bank_account.deposit("invalid")

    def test_withdraw_invalid(self):
        """Test withdrawing a non-numeric value."""
        with self.assertRaises(ValueError):
            self.bank_account.withdraw("invalid")

if __name__ == "__main__":
    unittest.main()