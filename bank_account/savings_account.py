from datetime import date
from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.9.0"

class SavingsAccount(BankAccount):
    """Class representing a savings account, inheriting from BankAccount."""
    SERVICE_CHARGE_PREMIUM = 2.0

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

    def get_service_charges(self):
        """Calculate service charges for the savings account.

        Returns:
            float: The calculated service charges based on the balance and minimum balance.
        """
        service_charge = self.BASE_SERVICE_CHARGE
        if self._balance < self.__minimum_balance:
            service_charge *= self.SERVICE_CHARGE_PREMIUM
        return service_charge

    def __str__(self):
        """Return a string representation of the SavingsAccount.

        Returns:
            str: A formatted string containing account details, including minimum balance.
        """
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings")