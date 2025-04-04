from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"

class ServiceChargeStrategy(ABC):
    """Abstract base class for service charge calculation strategies."""

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculate service charges based on the account."""
        pass