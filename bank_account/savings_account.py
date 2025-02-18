"""
Description: This file contains the SavingsAccount class.
Author: Md Apurba Khan
"""

from datetime import date

from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.5.2"


class SavingsAccount(BankAccount):
    """
    Represents a savings account with a minimum balance requirement.
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date = None,
        minimum_balance: float = 50.0,
    ):
        """
        Initializes a SavingsAccount.

        Args:
            account_number (int): Unique account identifier.
            client_number (int): Unique client identifier.
            balance (float): Initial balance.
            date_created (date, optional): Account creation date.
            minimum_balance (float, optional): Minimum balance.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._minimum_balance = float(minimum_balance)

    def get_service_charges(self) -> float:
        """
        Calculates service charges for the account.

        Returns:
            float: Service charge amount.
        """
        if self._balance >= self._minimum_balance:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the account.

        Returns:
            str: Account details.
        """
        base_str = super().__str__()
        return (
            f"{base_str}\n"
            f"Minimum Balance: ${self._minimum_balance:.2f}\n"
            f"Account Type: Savings"
        )
