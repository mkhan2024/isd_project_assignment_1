"""Description: This file contains the BankAccount class for the banking application.
Author: Md Apurba Khan"""

class BankAccount:
    def __init__(self, account_number, client_number, balance):
        """
        Initialize a BankAccount object. 

        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client number of the bank account.
            balance (float): The balance of the bank account.

        Raises:
            ValueError: If the account_number or client_number is not an integer, or if balance is not a float.
        """
        if not isinstance(account_number, int) or account_number < 10000:
            raise ValueError("Account number must be an integer of at least 10000")
        self._account_number = account_number

        if not isinstance(client_number, int) or client_number < 1000:
            raise ValueError("Client number must be an integer of at least 1000")
        self._client_number = client_number

        try:
            balance_float = float(balance)
            if balance_float < 0:
                raise ValueError("Balance must be non-negative")
            self._balance = balance_float
        except ValueError:
            raise ValueError("Balance must be a non-negative float")
        
    @property
    def account_number(self):
        return self._account_number

    @property
    def client_number(self):
        return self._client_number

    @property
    def balance(self):
        return self._balance
    
    def update_balance(self, amount):
        """
        Update the balance of the bank account.

        Args:
            amount (float): The amount to be deposited or withdrawn.
        """
        try:
            self._balance += float(amount)
        except ValueError:
            raise ValueError("Amount must be a numeric value")

    def deposit(self, amount):
        """
        Deposit money into the bank account.

        Args:
            amount (float): The amount to be deposited.

        Raises:
            ValueError: If the amount is not a float.
        """
        try:
            float_amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount must be numeric: {amount}")
        
        if float_amount <= 0:
            raise ValueError(f"Deposit amount must be positive: {amount}")
        self._balance += float_amount

    def withdraw(self, amount):
        """
        Withdraw money from the bank account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the amount is not numeric, or if the amount exceeds the balance.
        """
        try:
            float_amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount must be numeric: {amount}")
        
        if float_amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive: {amount}")
        if float_amount > self._balance:
            raise ValueError(f"Withdrawal amount exceeds account balance: {amount}")
        self._balance -= float_amount
        
    def __str__(self):
        return f"Account number: {self._account_number}\nClient number: {self._client_number}\nBalance: {self._balance:.2f}"