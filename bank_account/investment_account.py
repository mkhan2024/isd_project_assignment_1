"""
Description: This file defines the InvestmentAccount class,
which extends BankAccount.
Author: Md Apurba Khan
"""

from datetime import date, timedelta

from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"


class InvestmentAccount(BankAccount):
    """Represents an investment account with management fees."""

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        management_fee: float,
    ):
        """
        Initializes an investment account.

        Args:
            account_number (int): Account number.
            client_number (int): Client number.
            balance (float): Initial balance.
            date_created (date): Date account was created.
            management_fee (float): Flat-rate management fee.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Validate management fee
        try:
            self._management_fee = float(management_fee)
        except ValueError:
            self._management_fee = 2.55  # Default management fee if invalid

    def get_service_charges(self) -> float:
        """
        Calculates the service charge based on account age.

        Returns:
            float: Calculated service charge.
        """
        base_charge = 0.50
        if self._date_created > InvestmentAccount.TEN_YEARS_AGO:
            # Apply management fee if account is under 10 years old
            return base_charge + self._management_fee
        return base_charge  # Fee waived for accounts older than 10 years
