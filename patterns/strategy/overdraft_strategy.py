from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.2.0"

class OverdraftStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges for chequing accounts with overdraft."""

    def __init__(self, overdraft_rate: float, overdraft_limit: float) -> None:
        """Initialize the OverdraftStrategy with specific attributes."""
        self.__overdraft_rate = overdraft_rate
        self.__overdraft_limit = overdraft_limit

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculate service charges for the chequing account."""
        service_charge = self.BASE_SERVICE_CHARGE
        balance = account.balance
        if balance < 0:
            overdraft_amount = abs(balance)
            service_charge += overdraft_amount * self.__overdraft_rate
        return service_charge