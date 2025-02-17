"""
Description: Unit tests for the InvestmentAccount class.
Author: Md Apurba Khan
"""

import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

__author__ = "Md Apurba Khan"
__version__ = "1.0.0"

class TestInvestmentAccount(unittest.TestCase):
    """Tests the functionality of the InvestmentAccount class."""

    def setUp(self):
        """Set up test InvestmentAccount instances."""
        self.new_account = InvestmentAccount(5001, 1001, 5000, date.today(), 2.00)
        self.old_account = InvestmentAccount(5002, 1002, 10000, date.today() - timedelta(days=3653), 2.00)

    def test_service_charges_new_account(self):
        """Test service charges for accounts created within last 10 years."""
        self.assertEqual(self.new_account.get_service_charges(), 2.50)

    def test_service_charges_old_account(self):
        """Test service charges for accounts older than 10 years."""
        self.assertEqual(self.old_account.get_service_charges(), 0.50)

if __name__ == "__main__":
    unittest.main()