from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

__author__ = "Md Apurba Khan"
__version__ = "2.2.0"

class SavingsAccount(BankAccount):
    """Class representing a savings account, inheriting from BankAccount."""

    def __init__(self, account_number: str, client_number: str, balance: float, 
                 date_created: date, minimum_balance: float) -> None:
        """Initialize a SavingsAccount instance."""
        super().__init__(account_number, client_number, balance, date_created)
        self.__minimum_balance = float(minimum_balance) if self._is_valid_float(minimum_balance) else 50.0
        self.__service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def deposit(self, amount: float) -> None:
        """Deposit an amount into the savings account."""
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """Withdraw an amount from the savings account."""
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        amount = float(amount)
        if self._balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        """Calculate service charges for the savings account."""
        return self.__service_charge_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return a string representation of the SavingsAccount."""
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings")