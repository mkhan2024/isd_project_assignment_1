"""
Description: Unit tests for the InvestmentAccount class.
Author: Md Apurba Khan
"""

import unittest
from datetime import date, timedelta

from bank_account.investment_account import InvestmentAccount

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"


class TestInvestmentAccount(unittest.TestCase):
    """Tests the functionality of the InvestmentAccount class."""

    def setUp(self):
        """Set up test InvestmentAccount instances."""
        self.new_account = InvestmentAccount(
            5001, 1001, 5000, date.today(), 2.00
        )
        self.old_account = InvestmentAccount(
            5002, 1002, 10000, date.today() - timedelta(days=3653), 2.00
        )

    def test_service_charges_new_account(self):
        """Test service charges for accounts created within last 10 years."""
        self.assertEqual(self.new_account.get_service_charges(), 2.50)

    def test_service_charges_old_account(self):
        """Test service charges for accounts older than 10 years."""
        self.assertEqual(self.old_account.get_service_charges(), 0.50)

    def test_deposit_valid(self):
        """Test deposit of a valid amount."""
        self.new_account.deposit(200)
        self.assertEqual(self.new_account.balance, 5200)

    def test_deposit_invalid(self):
        """Test deposit of a non-numeric value."""
        with self.assertRaises(ValueError):
            self.new_account.deposit("invalid")

    def test_withdraw_valid(self):
        """Test withdrawing a valid amount."""
        self.new_account.withdraw(500)
        self.assertEqual(self.new_account.balance, 4500)

    def test_withdraw_exceeding_balance(self):
        """Test withdrawing more than balance raises error."""
        with self.assertRaises(ValueError):
            self.new_account.withdraw(6000)

    def test_management_fee_default(self):
        """Test default management fee when invalid value is given."""
        default_account = InvestmentAccount(
            5003, 1003, 3000, date.today(), "invalid"
        )
        self.assertEqual(default_account._management_fee, 2.55)


if __name__ == "__main__":
    unittest.main()
