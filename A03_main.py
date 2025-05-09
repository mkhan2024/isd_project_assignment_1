"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.7.0"
__credits__ = "Md Apurba Khan"

from bank_account import *
from datetime import date
from client.client import Client

def main():
    """Test the banking application with Observer Pattern."""
    client1 = Client(1001, "John", "Doe", "john.doe@example.com")
    chequing = ChequingAccount("CHK123", "1001", 500.00, date(2023, 1, 1), -1000.00, 0.05)
    savings1 = SavingsAccount("SAV123", "1001", 200.00, date(2023, 1, 1), 500.00)
    chequing.attach(client1)
    savings1.attach(client1)
    client2 = Client(1002, "Jane", "Smith", "jane.smith@example.com")
    savings2 = SavingsAccount("SAV124", "1002", 1000.00, date(2023, 1, 1), 500.00)
    savings2.attach(client2)

    try:
        chequing.deposit(15000.00)
    except ValueError as e:
        print(f"Chequing deposit error: {e}")

    try:
        chequing.withdraw(16000.00)
    except ValueError as e:
        print(f"Chequing withdraw error: {e}")

    try:
        chequing.deposit(50.00)
    except ValueError as e:
        print(f"Chequing deposit error: {e}")

    try:
        savings1.withdraw(150.00)
    except ValueError as e:
        print(f"Savings1 withdraw error: {e}")

    try:
        savings1.deposit(200.00)
    except ValueError as e:
        print(f"Savings1 deposit error: {e}")

    try:
        savings1.withdraw(50.00)
    except ValueError as e:
        print(f"Savings1 withdraw error: {e}")

    try:
        savings2.deposit(20000.00)
    except ValueError as e:
        print(f"Savings2 deposit error: {e}")

    try:
        savings2.withdraw(20000.00)
    except ValueError as e:
        print(f"Savings2 withdraw error: {e}")

    try:
        savings2.withdraw(950.00)
    except ValueError as e:
        print(f"Savings2 withdraw error: {e}")

if __name__ == "__main__":
    main()