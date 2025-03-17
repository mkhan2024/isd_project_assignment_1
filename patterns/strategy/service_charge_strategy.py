from abc import ABC, abstractmethod

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"

class ServiceChargeStrategy(ABC):
    """Abstract base class for service charge calculation strategies.

    Attributes:
        BASE_SERVICE_CHARGE (float): The base service charge applied to all accounts.
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, balance):
        """Calculate service charges based on the account balance.

        Args:
            balance (float): The current balance of the account.

        Returns:
            float: The calculated service charge.
        """
        pass