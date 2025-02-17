"""
Description: Unit tests for the ChequingAccount class.
Author: Md Apurba Khan
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

__author__ = "Md Apurba Khan"
__version__ = "1.0.0"

class TestChequingAccount(unittest.TestCase):
    """Tests the functionality of the ChequingAccount class."""

    def setUp(self):
        """Set up a test ChequingAccount instance."""
        self.account = ChequingAccount(3001, 1001, -600, date.today(), -100, 0.05)

    def test_service_charges_overdraft(self):
        """Test service charges when in overdraft."""
        self.assertEqual(round(self.account.get_service_charges(), 2), 25.50)

    def test_service_charges_no_overdraft(self):
        """Test service charges when not in overdraft."""
        self.account.deposit(600)  # Bring balance above overdraft limit
        self.assertEqual(self.account.get_service_charges(), 0.50)

if __name__ == "__main__":
    unittest.main()