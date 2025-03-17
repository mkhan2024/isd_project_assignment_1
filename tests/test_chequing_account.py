import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class TestChequingAccount(unittest.TestCase):
    """Test case for the ChequingAccount class."""

    def setUp(self):
        """Set up a chequing account instance before each test."""
        self.account = ChequingAccount("CHK123", "C001", 500.00, date(2023, 1, 1), -1000.00, 0.05)

    def test_service_charges_no_overdraft(self):
        """Test service charges when balance is above overdraft limit."""
        self.assertEqual(self.account.get_service_charges(), 0.50)  # BASE_SERVICE_CHARGE

    def test_service_charges_with_overdraft(self):
        """Test service charges when balance is below overdraft limit."""
        self.account.withdraw(1500.00)  # Balance = -1000.00
        expected_charge = 0.50 + (1000.00 * 0.05)  # BASE_SERVICE_CHARGE + overdraft fee (500 * 0.05)
        self.assertEqual(self.account.get_service_charges(), expected_charge)

if __name__ == "__main__":
    unittest.main()