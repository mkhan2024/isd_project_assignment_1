from datetime import date
from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.8.0"

class ChequingAccount(BankAccount):
    """Class representing a chequing account, inheriting from BankAccount."""

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

    def get_service_charges(self):
        """Calculate service charges for the chequing account.

        Returns:
            float: The calculated service charges based on the balance, overdraft limit, and rate.
        """
        service_charge = self.BASE_SERVICE_CHARGE
        if self._balance < self.__overdraft_limit:
            overdraft_amount = abs(self.__overdraft_limit - self._balance)
            service_charge += overdraft_amount * self.__overdraft_rate
        return service_charge

    def __str__(self):
        """Return a string representation of the ChequingAccount.

        Returns:
            str: A formatted string containing account details, including overdraft limit and rate.
        """
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate:.2%} Account Type: Cheq")