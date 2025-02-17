"""
Description: Unit tests for the SavingsAccount class.
Author: Md Apurba Khan
"""

import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

__author__ = "Md Apurba Khan"
__version__ = "1.0.0"

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

if __name__ == "__main__":
    unittest.main()