from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges for savings accounts."""

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float) -> None:
        """Initialize the MinimumBalanceStrategy with specific attributes."""
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculate service charges for the savings account."""
        service_charge = self.BASE_SERVICE_CHARGE
        if account.balance < self.__minimum_balance:
            service_charge *= self.SERVICE_CHARGE_PREMIUM
        return service_charge