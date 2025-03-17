from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

__author__ = "Md Apurba Khan"
__version__ = "1.7.0"

class InvestmentAccount(BankAccount):
    """Class representing an investment account, inheriting from BankAccount.

    Attributes:
        __service_charge_strategy (ManagementFeeStrategy): The strategy for calculating service charges.
        __management_fee (float): The flat-rate fee for managing the account.
    """

    def __init__(self, account_number, client_number, balance, date_created, management_fee):
        """Initialize an InvestmentAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            balance (float): The initial balance.
            date_created (date): The date the account was created.
            management_fee (float): The flat-rate fee for managing the account.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self.__management_fee = float(management_fee) if self._is_valid_float(management_fee) else 2.55
        self.__service_charge_strategy = ManagementFeeStrategy(self.__management_fee, self._date_created)

    def deposit(self, amount):
        """Deposit an amount into the investment account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._balance += float(amount)

    def withdraw(self, amount):
        """Withdraw an amount from the investment account.

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
        self._balance -= amount

    def get_service_charges(self):
        """Calculate service charges for the investment account.

        Delegates to the ManagementFeeStrategy to compute charges based on management fee and account age.

        Returns:
            float: The calculated service charges.
        """
        return self.__service_charge_strategy.calculate_service_charges(self._balance)

    def __str__(self):
        """Return a string representation of the InvestmentAccount.

        Returns:
            str: A formatted string containing account details, including management fee.
        """
        management_fee_str = "Waived" if self._date_created <= self.__service_charge_strategy.TEN_YEARS_AGO else f"${self.__management_fee:,.2f}"
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Date Created: {self._date_created} "
                f"Management Fee: {management_fee_str} Account Type: Inve")