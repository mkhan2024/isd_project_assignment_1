import unittest
from datetime import date

from bank_account.bank_account import BankAccount

"""
Description: Unit tests for the BankAccount class.
Author: Md Apurba Khan
"""


class TestableBankAccount(BankAccount):
    """
    A dummy subclass of BankAccount used for testing.
    Implements the abstract method `get_service_charges()`.
    """

    def get_service_charges(self):
        """Implements a basic service charge method for testing."""
        return self.BASE_SERVICE_CHARGE


class TestBankAccount(unittest.TestCase):
    """Tests the functionality of the BankAccount class."""

    def setUp(self):
        """Set up a test instance using TestableBankAccount."""
        self.bank_account = TestableBankAccount(
            2001, 1001, 1000.00, date.today()
        )

    def test_valid_bank_account(self):
        """Test bank account initialization with valid values."""
        self.assertEqual(self.bank_account.account_number, 2001)
        self.assertEqual(self.bank_account.client_number, 1001)
        self.assertEqual(self.bank_account.balance, 1000.00)

    def test_invalid_account_number(self):
        """Test bank account creation with an invalid account number."""
        with self.assertRaises(ValueError) as context:
            TestableBankAccount("invalid", 1001, 1000.00)
        self.assertEqual(
            str(context.exception), "Account number must be an integer."
        )

    def test_invalid_client_number(self):
        """Test bank account creation with an invalid client number."""
        with self.assertRaises(ValueError) as context:
            TestableBankAccount(2001, "invalid", 1000.00)
        self.assertEqual(
            str(context.exception), "Client number must be an integer."
        )

    def test_invalid_balance(self):
        """Test bank account creation with an invalid balance."""
        with self.assertRaises(ValueError) as context:
            TestableBankAccount(2001, 1001, "invalid_balance")
        self.assertEqual(
            str(context.exception), "Balance must be a numeric value."
        )

    def test_deposit_invalid(self):
        """Test deposit of a non-numeric value."""
        with self.assertRaises(ValueError) as context:
            self.bank_account.deposit("invalid")
        self.assertEqual(
            str(context.exception), "Deposit amount must be numeric."
        )

    def test_withdraw_invalid(self):
        """Test withdrawing a non-numeric value."""
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw("invalid")
        self.assertEqual(
            str(context.exception), "Withdrawal amount must be numeric."
        )


if __name__ == "__main__":
    unittest.main()
