from datetime import date, timedelta
from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.6.0"

class InvestmentAccount(BankAccount):
    """Class representing an investment account, inheriting from BankAccount."""
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

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

    def get_service_charges(self):
        """Calculate service charges for the investment account.

        Returns:
            float: The calculated service charges, considering the management fee and account age.
        """
        service_charge = self.BASE_SERVICE_CHARGE
        if self._date_created > self.TEN_YEARS_AGO:
            service_charge += self.__management_fee
        return service_charge

    def __str__(self):
        """Return a string representation of the InvestmentAccount.

        Returns:
            str: A formatted string containing account details, including management fee.
        """
        management_fee_str = "Waived" if self._date_created <= self.TEN_YEARS_AGO else f"${self.__management_fee:,.2f}"
        return (f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
                f"Date Created: {self._date_created} "
                f"Management Fee: {management_fee_str} Account Type: Inve")