from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

__author__ = "Md Apurba Khan"
__version__ = "2.2.0"

class SavingsAccount(BankAccount):
    """Class representing a savings account, inheriting from BankAccount.

    Attributes:
        __service_charge_strategy (MinimumBalanceStrategy): The strategy for calculating service charges.
        __minimum_balance (float): The minimum balance before additional charges apply.
    """

    def __init__(self, account_number, client_number, balance, date_created, minimum_balance):
        """Initialize a SavingsAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            balance (float): The initial balance.
            date_created (date): The date the account was created.
            minimum_balance (float): The minimum balance before additional charges apply.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self.__minimum_balance = float(minimum_balance) if self._is_valid_float(minimum_balance) else 50.0
        self.__service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def deposit(self, amount):
        """Deposit an amount into the savings account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.update_balance(amount)

    def withdraw(self, amount):
        """Withdraw an amount from the savings account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not a positive number or if there are insufficient funds.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        amount = float(amount)
        if self._balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self.update_balance(-amount)

    def get_service_charges(self):
        """Calculate service charges for the savings account.

        Delegates to the MinimumBalanceStrategy to compute charges based on balance and minimum balance.

        Returns:
            float: The calculated service charges.
        """
        return self.__service_charge_strategy.calculate_service_charges(self._balance)

    def __str__(self):
        """Return a string representation of the SavingsAccount.

        Returns:
            str: A formatted string containing account details, including minimum balance.
        """
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings")