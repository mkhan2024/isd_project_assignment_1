import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

__author__ = "Md Apurba Khan"
__version__ = "1.2.0"

class TestChequingAccount(unittest.TestCase):
    """Test case for the ChequingAccount class."""

    def setUp(self):
        """Set up test fixtures."""
        self.account = ChequingAccount("1234567", "C001", 1559.49, date(2024, 1, 1), -100.0, 0.05)

    def test_init_valid_inputs(self):
        """Test initialization with valid inputs."""
        self.assertEqual(self.account.account_number, "1234567")  # Use property getter
        self.assertEqual(self.account.balance, 1559.49)          # Use property getter
        self.assertEqual(self.account._ChequingAccount__overdraft_limit, -100.0)
        self.assertEqual(self.account._ChequingAccount__overdraft_rate, 0.05)

    def test_init_invalid_overdraft_limit(self):
        """Test initialization with invalid overdraft limit."""
        account = ChequingAccount("1234567", "C001", 1559.49, date(2024, 1, 1), "invalid", 0.05)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.0)

    def test_init_invalid_overdraft_rate(self):
        """Test initialization with invalid overdraft rate."""
        account = ChequingAccount("1234567", "C001", 1559.49, date(2024, 1, 1), -100.0, "invalid")
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_init_invalid_date_created(self):
        """Test initialization with invalid date_created."""
        account = ChequingAccount("1234567", "C001", 1559.49, "invalid", -100.0, 0.05)
        self.assertEqual(account._date_created, date.today())  # Use protected attribute directly

    def test_get_service_charges_no_overdraft(self):
        """Test service charges when balance is above overdraft limit."""
        self.assertEqual(self.account.get_service_charges(), 0.50)

    def test_get_service_charges_with_overdraft(self):
        """Test service charges when balance is below overdraft limit."""
        overdraft_account = ChequingAccount("1234567", "C001", -600.0, date(2024, 1, 1), -100.0, 0.05)
        self.assertEqual(round(overdraft_account.get_service_charges(), 2), 25.50)

    def test_get_service_charges_at_overdraft_limit(self):
        """Test service charges when balance equals overdraft limit."""
        limit_account = ChequingAccount("1234567", "C001", -100.0, date(2024, 1, 1), -100.0, 0.05)
        self.assertEqual(limit_account.get_service_charges(), 0.50)

    def test_str(self):
        """Test string representation of the account."""
        expected = ("Account Number: 1234567 Balance: $1,559.49\n"
                    "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Cheq")
        self.assertEqual(str(self.account), expected)

if __name__ == "__main__":
    unittest.main()