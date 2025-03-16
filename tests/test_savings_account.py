import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"

class TestSavingsAccount(unittest.TestCase):
    """Test case for the SavingsAccount class."""

    def setUp(self):
        """Set up test fixtures."""
        self.account = SavingsAccount("9483914", "C004", 1559.49, date(2024, 1, 1), 50.0)

    def test_init_valid_inputs(self):
        """Test initialization with valid inputs."""
        self.assertEqual(self.account.account_number, "9483914")  # Use property getter
        self.assertEqual(self.account.balance, 1559.49)          # Use property getter
        self.assertEqual(self.account._SavingsAccount__minimum_balance, 50.0)

    def test_init_invalid_minimum_balance(self):
        """Test initialization with invalid minimum balance."""
        account = SavingsAccount("9483914", "C004", 1559.49, date(2024, 1, 1), "invalid")
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.0)

    def test_init_invalid_date_created(self):
        """Test initialization with invalid date_created."""
        account = SavingsAccount("9483914", "C004", 1559.49, "invalid", 50.0)
        self.assertEqual(account._date_created, date.today())  # Use protected attribute directly

    def test_get_service_charges_above_minimum(self):
        """Test service charges when balance is above minimum."""
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_get_service_charges_below_minimum(self):
        """Test service charges when balance is below minimum."""
        low_balance_account = SavingsAccount("9483914", "C004", 49.99, date(2024, 1, 1), 50.0)
        self.assertEqual(round(low_balance_account.get_service_charges(), 2), 1.00)

    def test_str(self):
        """Test string representation of the account."""
        expected = ("Account Number: 9483914 Balance: $1,559.49\n"
                    "Minimum Balance: $50.00 Account Type: Savings")
        self.assertEqual(str(self.account), expected)

if __name__ == "__main__":
    unittest.main()