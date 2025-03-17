import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

__author__ = "Md Apurba Khan"
__version__ = "1.6.0"

class TestSavingsAccount(unittest.TestCase):
    """Test case for the SavingsAccount class."""

    def setUp(self):
        """Set up a savings account instance before each test."""
        self.account = SavingsAccount("SAV123", "C001", 100.00, date(2023, 1, 1), 50.0)

    def test_service_charges_above_minimum(self):
        """Test service charges when balance is above minimum."""
        self.assertEqual(self.account.get_service_charges(), 0.50)  # BASE_SERVICE_CHARGE

    def test_service_charges_below_minimum(self):
        """Test service charges when balance is below minimum."""
        self.account.withdraw(60.00)  # Balance = 40.00, below 50.0
        self.assertEqual(self.account.get_service_charges(), 0.50 * 2.0)  # BASE_SERVICE_CHARGE * SERVICE_CHARGE_PREMIUM

if __name__ == "__main__":
    unittest.main()