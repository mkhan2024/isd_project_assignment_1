from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

__author__ = "Md Apurba Khan"
__version__ = "2.1.0"

class ChequingAccount(BankAccount):
    """Class representing a chequing account, inheriting from BankAccount."""

    def __init__(self, account_number: str, client_number: str, balance: float, 
                 date_created: date, overdraft_limit: float, overdraft_rate: float) -> None:
        """Initialize a ChequingAccount instance."""
        super().__init__(account_number, client_number, balance, date_created)
        self.__overdraft_limit = float(overdraft_limit) if self._is_valid_float(overdraft_limit) else -100.0
        self.__overdraft_rate = float(overdraft_rate) if self._is_valid_float(overdraft_rate) else 0.05
        self.__service_charge_strategy = OverdraftStrategy(self.__overdraft_rate, self.__overdraft_limit)

    def deposit(self, amount: float) -> None:
        """Deposit an amount into the chequing account."""
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """Withdraw an amount from the chequing account."""
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        amount = float(amount)
        if self._balance - amount < self.__overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        """Calculate service charges for the chequing account."""
        return self.__service_charge_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return a string representation of the ChequingAccount."""
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate:.2%} Account Type: Cheq")