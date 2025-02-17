import unittest
from bank_account.bank_account import BankAccount

"""
Description: Unit tests for the BankAccount class.
Author: Md Apurba Khan
Usage: To execute all tests in the terminal execute:
    python -m unittest tests/test_bank_account.py
"""


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Set up a test bank account instance."""
        self.bank_account = BankAccount(2001, 1001, 1000.00)

    def test_valid_bank_account(self):
        """Test bank account initialization with valid values."""
        self.assertEqual(self.bank_account.account_number, 2001)
        self.assertEqual(self.bank_account.client_number, 1001)
        self.assertEqual(self.bank_account.balance, 1000.00)

    def test_invalid_account_number(self):
        """Test bank account creation with invalid account number."""
        with self.assertRaises(ValueError):
            BankAccount("invalid", 1001, 1000.00)

    def test_invalid_client_number(self):
        """Test bank account creation with invalid client number."""
        with self.assertRaises(ValueError):
            BankAccount(2001, "invalid", 1000.00)

    def test_invalid_balance(self):
        """Test bank account creation with invalid balance."""
        with self.assertRaises(ValueError):
            BankAccount(2001, 1001, "invalid_balance")
        with self.assertRaises(ValueError):
            BankAccount(2002, 1002, None)

    def test_balance_defaults_to_zero(self):
        """Test if an invalid balance defaults to zero instead of raising an exception."""
        account = BankAccount(2003, 1002, 0)
        self.assertEqual(account.balance, 0.0)

    def test_deposit_valid(self):
        """Test deposit of valid amount."""
        self.bank_account.deposit(500.00)
        self.assertEqual(self.bank_account.balance, 1500.00)

    def test_deposit_invalid(self):
        """Test deposit of non-numeric value."""
        with self.assertRaises(ValueError):
            self.bank_account.deposit("invalid")

    def test_deposit_negative(self):
        """Test deposit of negative amount."""
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-100)

    def test_withdraw_valid(self):
        """Test withdrawing a valid amount."""
        self.bank_account.withdraw(500.00)
        self.assertEqual(self.bank_account.balance, 500.00)

    def test_withdraw_entire_balance(self):
        """Test withdrawing the entire balance sets it to zero."""
        self.bank_account.withdraw(1000.00)
        self.assertEqual(self.bank_account.balance, 0.00)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than the balance."""
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(2000.00)

    def test_withdraw_invalid(self):
        """Test withdrawing a non-numeric value."""
        with self.assertRaises(ValueError):
            self.bank_account.withdraw("invalid")

    def test_withdraw_negative(self):
        """Test withdrawing a negative amount."""
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-100)

    def test_update_balance_positive(self):
        """Test updating balance with a positive amount."""
        self.bank_account.update_balance(250.00)
        self.assertEqual(self.bank_account.balance, 1250.00)

    def test_update_balance_negative(self):
        """Test updating balance with a negative amount (simulating a withdrawal)."""
        self.bank_account.update_balance(-150.00)
        self.assertEqual(self.bank_account.balance, 850.00)

    def test_str_method(self):
        """Test the __str__ method of BankAccount."""
        expected = "Account Number: 2001 Balance: $1,000.00"
        self.assertEqual(str(self.bank_account), expected)


if __name__ == "__main__":
    unittest.main()
