"""
Description: This file defines the ChequingAccount class,
which extends BankAccount.
Author: Md Apurba Khan
"""

from datetime import date

from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.2.0"


class ChequingAccount(BankAccount):
    """Represents a chequing account with overdraft features."""

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        overdraft_limit: float,
        overdraft_rate: float,
    ):
        """
        Initializes a chequing account with overdraft handling.

        Args:
            account_number (int): Account number.
            client_number (int): Client number.
            balance (float): Initial balance.
            date_created (date): Date account was created.
            overdraft_limit (float): Maximum overdraft allowed.
            overdraft_rate (float): Overdraft fee rate.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Validate overdraft limit
        try:
            self._overdraft_limit = float(overdraft_limit)
        except ValueError:
            self._overdraft_limit = -100  # Default value if invalid

        # Validate overdraft rate
        try:
            self._overdraft_rate = float(overdraft_rate)
        except ValueError:
            self._overdraft_rate = 0.05  # Default overdraft rate

    def withdraw(self, amount: float):
        """
        Withdraws money from the account, considering overdraft limit.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If the withdrawal exceeds overdraft limit.
        """
        if amount <= 0:
            raise ValueError(
                f"Withdrawal amount must be positive: ${amount:.2f}"
            )

        # Simulate new balance after withdrawal
        new_balance = self._balance - amount

        # ✅ **Fixed Logic: Allow withdrawal within overdraft limit**
        if new_balance < self._overdraft_limit:
            raise ValueError(
                f"Cannot withdraw ${amount:.2f}. "
                f"Overdraft limit of ${self._overdraft_limit:.2f} exceeded."
            )

        self._balance = new_balance  # Perform withdrawal

    def get_service_charges(self) -> float:
        """
        Calculates the service charge based on overdraft.

        Returns:
            float: Calculated service charge.
        """
        if self._balance < 0:  # Check if account is in overdraft
            # Calculate how much the account is overdrawn
            overdraft_amount = abs(self._balance)
            return (
                overdraft_amount * self._overdraft_rate
            )  # Charge on overdraft
        return 0.50  # Default service charge when not in overdraft

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the chequing account.

        Returns:
            str: Account details with overdraft info.
        """
        return (
            f"Account Number: {self._account_number} "
            f"Balance: ${self._balance:,.2f}\n"
            f"Overdraft Limit: ${self._overdraft_limit:.2f} "
            f"Overdraft Rate: {self._overdraft_rate * 100:.2f}% "
            f"Account Type: Chequing"
        )
