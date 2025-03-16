import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class TestInvestmentAccount(unittest.TestCase):
    """Test case for the InvestmentAccount class."""

    def setUp(self):
        """Set up test fixtures."""
        self.new_account = InvestmentAccount("2341234", "C002", 19329.21, date(2024, 1, 1), 1.99)
        self.old_account = InvestmentAccount("1948371", "C003", 11329.65, date(2013, 1, 1), 2.00)

    def test_init_valid_inputs(self):
        """Test initialization with valid inputs."""
        self.assertEqual(self.new_account.account_number, "2341234")  # Use property getter
        self.assertEqual(self.new_account.balance, 19329.21)         # Use property getter
        self.assertEqual(self.new_account._InvestmentAccount__management_fee, 1.99)

    def test_init_invalid_management_fee(self):
        """Test initialization with invalid management fee."""
        account = InvestmentAccount("2341234", "C002", 19329.21, date(2024, 1, 1), "invalid")
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_init_invalid_date_created(self):
        """Test initialization with invalid date_created."""
        account = InvestmentAccount("2341234", "C002", 19329.21, "invalid", 1.99)
        self.assertEqual(account._date_created, date.today())  # Use protected attribute directly

    def test_get_service_charges_new_account(self):
        """Test service charges for a new account."""
        self.assertEqual(round(self.new_account.get_service_charges(), 2), 2.49)

    def test_get_service_charges_old_account(self):
        """Test service charges for an old account (fee waived)."""
        self.assertEqual(round(self.old_account.get_service_charges(), 2), 0.50)

    def test_str_new_account(self):
        """Test string representation for a new account."""
        expected = ("Account Number: 2341234 Balance: $19,329.21\n"
                    "Date Created: 2024-01-01 Management Fee: $1.99 Account Type: Inve")
        self.assertEqual(str(self.new_account), expected)

    def test_str_old_account(self):
        """Test string representation for an old account."""
        expected = ("Account Number: 1948371 Balance: $11,329.65\n"
                    "Date Created: 2013-01-01 Management Fee: Waived Account Type: Inve")
        self.assertEqual(str(self.old_account), expected)

if __name__ == "__main__":
    unittest.main()