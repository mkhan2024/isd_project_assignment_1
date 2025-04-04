from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

__author__ = "Md Apurba Khan"
__version__ = "1.7.0"

class InvestmentAccount(BankAccount):
    """Class representing an investment account, inheriting from BankAccount."""

    def __init__(self, account_number: str, client_number: str, balance: float, 
                 date_created: date, management_fee: float) -> None:
        """Initialize an InvestmentAccount instance."""
        super().__init__(account_number, client_number, balance, date_created)
        self.__management_fee = float(management_fee) if self._is_valid_float(management_fee) else 2.55
        self.__service_charge_strategy = ManagementFeeStrategy(self.__management_fee, self._date_created)

    def deposit(self, amount: float) -> None:
        """Deposit an amount into the investment account."""
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.update_balance(float(amount))

    def withdraw(self, amount: float) -> None:
        """Withdraw an amount from the investment account."""
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        amount = float(amount)
        if self._balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self.update_balance(-amount)

    def get_service_charges(self) -> float:
        """Calculate service charges for the investment account."""
        return self.__service_charge_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return a string representation of the InvestmentAccount."""
        management_fee_str = "Waived" if self._date_created <= self.__service_charge_strategy.TEN_YEARS_AGO else f"${self.__management_fee:,.2f}"
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Date Created: {self._date_created} "
                f"Management Fee: {management_fee_str} Account Type: Inve")