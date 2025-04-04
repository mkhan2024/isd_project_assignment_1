from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class ManagementFeeStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges for investment accounts."""

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee: float, account_open_date: date) -> None:
        """Initialize the ManagementFeeStrategy with specific attributes."""
        self.__management_fee = management_fee
        self.__account_open_date = account_open_date

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculate service charges for the investment account."""
        service_charge = self.BASE_SERVICE_CHARGE
        if self.__account_open_date > self.TEN_YEARS_AGO:
            service_charge += self.__management_fee
        return service_charge