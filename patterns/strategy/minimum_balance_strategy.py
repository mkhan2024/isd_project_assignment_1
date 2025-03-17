from .service_charge_strategy import ServiceChargeStrategy

__author__ = "Md Apurba Khan"
__version__ = "1.4.0"

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges for savings accounts.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): The factor by which the base service charge is multiplied if the balance is below the minimum.
        __minimum_balance (float): The minimum balance required to avoid premium charges.
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance):
        """Initialize the MinimumBalanceStrategy with specific attributes.

        Args:
            minimum_balance (float): The minimum balance required to avoid premium charges.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, balance):
        """Calculate service charges for the savings account.

        If the balance is below the minimum, the base service charge is multiplied by the premium factor.
        Otherwise, the base service charge is applied.

        Args:
            balance (float): The current balance of the account.

        Returns:
            float: The calculated service charge.
        """
        service_charge = self.BASE_SERVICE_CHARGE
        if balance < self.__minimum_balance:
            service_charge *= self.SERVICE_CHARGE_PREMIUM
        return service_charge