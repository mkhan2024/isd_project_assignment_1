"""
Description: A client program written to verify correctness of 
the BankAccount subclasses.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Md Apurba Khan"

# 1. Import all BankAccount types using the bank_account package
#    Import date from datetime
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
#    choice including a balance which is below the overdraft limit.
chequing = ChequingAccount(3001, 1001, -200, date.today(), -100, 0.05)

# 3. Print the ChequingAccount created in step 2.
print(chequing)

# 3b. Print the service charges amount if calculated based on the 
#     current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
#     enough money into the chequing account to avoid overdraft fees.
chequing.deposit(300)

# 4b. Print the ChequingAccount
print(chequing)

# 4c. Print the service charges amount if calculated based on the 
#     current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing.get_service_charges())

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
#    choice including a balance which is above the minimum balance.
savings = SavingsAccount(4001, 1001, 60, date.today(), 50)

# 6. Print the SavingsAccount created in step 5.
print(savings)

# 6b. Print the service charges amount if calculated based on the 
#     current state of the SavingsAccount created in step 5.
print("Service Charges:", savings.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
#     enough money from the savings account to cause the balance to fall 
#     below the minimum balance.
savings.withdraw(20)

# 7b. Print the SavingsAccount.
print(savings)

# 7c. Print the service charges amount if calculated based on the 
#     current state of the SavingsAccount created in step 5.
print("Service Charges:", savings.get_service_charges())

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
#    choice including a date created within the last 10 years.
investment_new = InvestmentAccount(5001, 1001, 5000, date.today(), 2.00)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_new)

# 9b. Print the service charges amount if calculated based on the 
#     current state of the InvestmentAccount created in step 8.
print("Service Charges:", investment_new.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
#     choice including a date created prior to 10 years ago.
investment_old = InvestmentAccount(5002, 1002, 10000, date.today() - timedelta(days=3653), 2.00)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_old)

# 11b. Print the service charges amount if calculated based on the 
#     current state of the InvestmentAccount created in step 10.
print("Service Charges:", investment_old.get_service_charges())

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
#     by using the withdraw method of the superclass and withdrawing 
#     the service charges determined by each instance invoking the 
#     polymorphic get_service_charges method.
chequing.withdraw(chequing.get_service_charges())
savings.withdraw(savings.get_service_charges())
investment_new.withdraw(investment_new.get_service_charges())
investment_old.withdraw(investment_old.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing)
print(savings)
print(investment_new)
print(investment_old)