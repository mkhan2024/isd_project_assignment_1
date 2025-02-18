"""
Description: Unit tests for the SavingsAccount class.
Author: Md Apurba Khan
"""

import unittest
from datetime import date

from bank_account.savings_account import SavingsAccount

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"


class TestSavingsAccount(unittest.TestCase):
    """Tests the functionality of the SavingsAccount class."""

    def setUp(self):
        """Set up a test SavingsAccount instance."""
        self.account = SavingsAccount(4001, 1001, 40, date.today(), 50)

    def test_service_charges_below_minimum(self):
        """Test service charges when below minimum balance."""
        self.assertEqual(self.account.get_service_charges(), 1.00)

    def test_service_charges_above_minimum(self):
        """Test service charges when above minimum balance."""
        self.account.deposit(20)  # Bring balance above minimum
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_deposit_valid(self):
        """Test deposit of a valid amount."""
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 140)

    def test_deposit_invalid(self):
        """Test deposit of a non-numeric value."""
        with self.assertRaises(ValueError):
            self.account.deposit("invalid")

    def test_withdraw_valid(self):
        """Test withdrawing a valid amount."""
        self.account.withdraw(20)
        self.assertEqual(self.account.balance, 20)

    def test_withdraw_below_minimum(self):
        """Test withdrawing below minimum balance triggers extra charge."""
        self.account.withdraw(10)  # New balance 30 (below 50)
        self.assertEqual(self.account.get_service_charges(), 1.00)

    def test_withdraw_exceeding_balance(self):
        """Test withdrawing more than balance raises error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(500)


if __name__ == "__main__":
    unittest.main()
