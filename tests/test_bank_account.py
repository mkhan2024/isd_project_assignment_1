"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(10001, 1001, 100.0)

    def test_init(self):
        self.assertEqual(self.bank_account.account_number, 10001)
        self.assertEqual(self.bank_account.client_number, 1001)
        self.assertEqual(self.bank_account.balance, 100.0)
        
    def test_invalid_account_number(self):
        with self.assertRaises(ValueError):
            BankAccount(999, 1001, 100.0)

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            BankAccount(10001, 999, 100.0)

    def test_invalid_balance(self):
        with self.assertRaises(ValueError):
            BankAccount(10001, 1001, "invalid")

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit("invalid")

    def test_invalid_withdraw(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw("invalid")

    def test_invalid_update_balance(self):
        with self.assertRaises(ValueError):
            self.bank_account.update_balance("invalid")

    def test_properties(self):
        self.assertEqual(self.bank_account.account_number, 10001)
        self.assertEqual(self.bank_account.client_number, 1001)
        self.assertEqual(self.bank_account.balance, 100.0)

    def test_update_balance(self):
        self.bank_account.update_balance(50.0)
        self.assertEqual(self.bank_account.balance, 150.0)

    def test_deposit(self):
        self.bank_account.deposit(50.0)
        self.assertEqual(self.bank_account.balance, 150.0)

    def test_withdraw(self):
        self.bank_account.withdraw(50.0)
        self.assertEqual(self.bank_account.balance, 50.0)

    def test_invalid_withdraw(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(150.0)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-50.0)

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-50.0)

    def test_str(self):
        expected = f"Account number: 10001\nClient number: 1001\nBalance: 100.00"
        self.assertEqual(str(self.bank_account), expected)

if __name__ == '__main__':
    unittest.main()