"""
Description: Unit tests for the ChequingAccount class.
Author: Md Apurba Khan
"""

import unittest
from datetime import date

from bank_account.chequing_account import ChequingAccount

__author__ = "Md Apurba Khan"
__version__ = "1.2.0"


class TestChequingAccount(unittest.TestCase):
    """Tests the functionality of the ChequingAccount class."""

    def setUp(self):
        """Set up a test ChequingAccount instance."""
        self.account = ChequingAccount(
            3001, 1001, -50, date.today(), -100, 0.05
        )

    def test_service_charges_overdraft(self):
        """Test service charges when in overdraft."""
        self.assertEqual(round(self.account.get_service_charges(), 2), 2.50)

    def test_service_charges_no_overdraft(self):
        """Test service charges when not in overdraft."""
        self.account.deposit(100)  # Bring balance above overdraft limit
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_deposit_valid(self):
        """Test deposit of a valid amount."""
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_invalid(self):
        """Test deposit of a non-numeric value."""
        with self.assertRaises(ValueError):
            self.account.deposit("invalid")

    def test_withdraw_valid(self):
        """Test withdrawing a valid amount within overdraft limit."""
        self.account.withdraw(30)
        # New balance should be within overdraft limit
        self.assertEqual(self.account.balance, -80)

    def test_withdraw_exceeding_limit(self):
        """Test withdrawing beyond overdraft limit."""
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

    def test_overdraft_limit_default(self):
        """Test default overdraft limit when invalid value is given."""
        default_account = ChequingAccount(
            3002, 1002, 0, date.today(), "invalid", 0.05
        )
        self.assertEqual(default_account._overdraft_limit, -100)


if __name__ == "__main__":
    unittest.main()
