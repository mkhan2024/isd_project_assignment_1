from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

__author__ = "Md Apurba Khan"
__version__ = "2.1.0"

class ChequingAccount(BankAccount):
    """Class representing a chequing account, inheriting from BankAccount.

    Attributes:
        __service_charge_strategy (OverdraftStrategy): The strategy for calculating service charges.
        __overdraft_limit (float): The maximum amount the balance can be overdrawn.
        __overdraft_rate (float): The rate at which overdraft fees are applied.
    """

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate):
        """Initialize a ChequingAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            balance (float): The initial balance.
            date_created (date): The date the account was created.
            overdraft_limit (float): The maximum amount the balance can be overdrawn.
            overdraft_rate (float): The rate at which overdraft fees are applied.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self.__overdraft_limit = float(overdraft_limit) if self._is_valid_float(overdraft_limit) else -100.0
        self.__overdraft_rate = float(overdraft_rate) if self._is_valid_float(overdraft_rate) else 0.05
        self.__service_charge_strategy = OverdraftStrategy(self.__overdraft_rate, self.__overdraft_limit)

    def deposit(self, amount):
        """Deposit an amount into the chequing account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.update_balance(amount)

    def withdraw(self, amount):
        """Withdraw an amount from the chequing account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not a positive number or exceeds the overdraft limit.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        amount = float(amount)
        if self._balance - amount < self.__overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        self.update_balance(-amount)

    def get_service_charges(self):
        """Calculate service charges for the chequing account.

        Delegates to the OverdraftStrategy to compute charges based on balance, overdraft limit, and rate.

        Returns:
            float: The calculated service charges.
        """
        return self.__service_charge_strategy.calculate_service_charges(self._balance)

    def __str__(self):
        """Return a string representation of the ChequingAccount.

        Returns:
            str: A formatted string containing account details, including overdraft limit and rate.
        """
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate:.2%} Account Type: Cheq")