from .service_charge_strategy import ServiceChargeStrategy

__author__ = "Md Apurba Khan"
__version__ = "1.2.0"

class OverdraftStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges for chequing accounts with overdraft.

    Attributes:
        __overdraft_rate (float): The rate at which overdraft fees are applied.
        __overdraft_limit (float): The maximum overdraft allowed.
    """

    def __init__(self, overdraft_rate, overdraft_limit):
        """Initialize the OverdraftStrategy with specific attributes.

        Args:
            overdraft_rate (float): The rate at which overdraft fees are applied.
            overdraft_limit (float): The maximum overdraft allowed.
        """
        self.__overdraft_rate = overdraft_rate
        self.__overdraft_limit = overdraft_limit

    def calculate_service_charges(self, balance):
        """Calculate service charges for the chequing account.

        If the balance is below the overdraft limit, an additional fee is applied based on the overdraft amount
        and rate.

        Args:
            balance (float): The current balance of the account.

        Returns:
            float: The calculated service charge.
        """
        service_charge = self.BASE_SERVICE_CHARGE
        if balance < self.__overdraft_limit:
            overdraft_amount = abs(self.__overdraft_limit - balance)
            service_charge += overdraft_amount * self.__overdraft_rate
        return service_charge