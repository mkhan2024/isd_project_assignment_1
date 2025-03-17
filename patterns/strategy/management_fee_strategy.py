from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class ManagementFeeStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges for investment accounts.

    Attributes:
        TEN_YEARS_AGO (date): The date representing ten years ago, used to determine fee waivers.
        __management_fee (float): The fee charged for account management.
        __account_open_date (date): The date the account was opened.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee, account_open_date):
        """Initialize the ManagementFeeStrategy with specific attributes.

        Args:
            management_fee (float): The fee charged for account management.
            account_open_date (date): The date the account was opened.
        """
        self.__management_fee = management_fee
        self.__account_open_date = account_open_date

    def calculate_service_charges(self, balance):
        """Calculate service charges for the investment account.

        If the account is older than ten years, no service charge is applied.
        Otherwise, the base service charge plus the management fee is applied.

        Args:
            balance (float): The current balance of the account.

        Returns:
            float: The calculated service charge.
        """
        service_charge = self.BASE_SERVICE_CHARGE
        if self.__account_open_date > self.TEN_YEARS_AGO:
            service_charge += self.__management_fee
        return service_charge