import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

__author__ = "Md Apurba Khan"
__version__ = "1.6.0"

class TestInvestmentAccount(unittest.TestCase):
    """Test case for the InvestmentAccount class."""

    def test_service_charges_new_account(self):
        """Test service charges for a new account (less than 10 years old)."""
        account = InvestmentAccount("INV123", "C001", 1000.00, date.today(), 2.55)
        self.assertEqual(account.get_service_charges(), 0.50 + 2.55)  # BASE_SERVICE_CHARGE + management_fee

    def test_service_charges_old_account(self):
        """Test service charges for an old account (over 10 years old)."""
        ten_years_ago = date.today() - timedelta(days=10 * 365.25 + 1)  # Ensure > 10 years
        account = InvestmentAccount("INV124", "C001", 1000.00, ten_years_ago, 2.55)
        self.assertEqual(account.get_service_charges(), 0.50)  # Only BASE_SERVICE_CHARGE (fee waived)

if __name__ == "__main__":
    unittest.main()