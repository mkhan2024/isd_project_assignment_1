"""
Description: A client program written to verify correctness of 
the BankAccount subclasses.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Md Apurba Khan"

# 1. Import all BankAccount types using the bank_account package
#    Import date from datetime
from bank_account import *
from datetime import date, timedelta

def main():
    """Main function to demonstrate the functionality of BankAccount subclasses."""
    # 2. Create an instance of a ChequingAccount with values of your 
    #    choice including a balance which is below the overdraft limit.
    try:
        chequing = ChequingAccount("3001", "1001", -200, date.today(), -100, 0.05)
    except Exception as e:
        print(f"Error creating ChequingAccount: {e}")

    # 3. Print the ChequingAccount created in step 2.
    print(chequing)

    # 3b. Print the service charges amount if calculated based on the 
    #     current state of the ChequingAccount created in step 2.
    try:
        print(f"Service Charges: ${chequing.get_service_charges():.2f}")
    except Exception as e:
        print(f"Error calculating service charges for ChequingAccount: {e}")

    # 4a. Use ChequingAccount instance created in step 2 to deposit 
    #     enough money into the chequing account to avoid overdraft fees.
    # try:
    #     chequing.deposit(300)
    # except Exception as e:
    #     print(f"Error depositing into ChequingAccount: {e}")

    # 4b. Print the ChequingAccount
    print(chequing)

    # 4c. Print the service charges amount if calculated based on the 
    #     current state of the ChequingAccount created in step 2.
    try:
        print(f"Service Charges: ${chequing.get_service_charges():.2f}")
    except Exception as e:
        print(f"Error calculating service charges for ChequingAccount: {e}")

    print("===================================================")

    # 5. Create an instance of a SavingsAccount with values of your 
    #    choice including a balance which is above the minimum balance.
    try:
        savings = SavingsAccount("4001", "1001", 60, date.today(), 50)
    except Exception as e:
        print(f"Error creating SavingsAccount: {e}")

    # 6. Print the SavingsAccount created in step 5.
    print(savings)

    # 6b. Print the service charges amount if calculated based on the 
    #     current state of the SavingsAccount created in step 5.
    try:
        print(f"Service Charges: ${savings.get_service_charges():.2f}")
    except Exception as e:
        print(f"Error calculating service charges for SavingsAccount: {e}")

    # 7a. Use this SavingsAccount instance created in step 5 to withdraw 
    #     enough money from the savings account to cause the balance to fall 
    #     below the minimum balance.
    # try:
    #     savings.withdraw(20)
    # except Exception as e:
    #     print(f"Error withdrawing from SavingsAccount: {e}")

    # 7b. Print the SavingsAccount.
    print(savings)

    # 7c. Print the service charges amount if calculated based on the 
    #     current state of the SavingsAccount created in step 5.
    try:
        print(f"Service Charges: ${savings.get_service_charges():.2f}")
    except Exception as e:
        print(f"Error calculating service charges for SavingsAccount: {e}")

    print("===================================================")

    # 8. Create an instance of an InvestmentAccount with values of your 
    #    choice including a date created within the last 10 years.
    try:
        investment_new = InvestmentAccount("5001", "1001", 5000, date.today(), 2.00)
    except Exception as e:
        print(f"Error creating InvestmentAccount (new): {e}")

    # 9a. Print the InvestmentAccount created in step 8.
    print(investment_new)

    # 9b. Print the service charges amount if calculated based on the 
    #     current state of the InvestmentAccount created in step 8.
    try:
        print(f"Service Charges: ${investment_new.get_service_charges():.2f}")
    except Exception as e:
        print(f"Error calculating service charges for InvestmentAccount (new): {e}")

    # 10. Create an instance of an InvestmentAccount with values of your 
    #     choice including a date created prior to 10 years ago.
    try:
        investment_old = InvestmentAccount("5002", "1002", 10000, date.today() - timedelta(days=3653), 2.00)
    except Exception as e:
        print(f"Error creating InvestmentAccount (old): {e}")

    # 11a. Print the InvestmentAccount created in step 10.
    print(investment_old)

    # 11b. Print the service charges amount if calculated based on the 
    #     current state of the InvestmentAccount created in step 10.
    try:
        print(f"Service Charges: ${investment_old.get_service_charges():.2f}")
    except Exception as e:
        print(f"Error calculating service charges for InvestmentAccount (old): {e}")

    print("===================================================")

    # 12. Update the balance of each account created in steps 2, 5, 8 and 10 
    #     by using the withdraw method of the superclass and withdrawing 
    #     the service charges determined by each instance invoking the 
    #     polymorphic get_service_charges method.
    # try:
    #     chequing.withdraw(chequing.get_service_charges())
    # except Exception as e:
    #     print(f"Error withdrawing service charges from ChequingAccount: {e}")
    # try:
    #     savings.withdraw(savings.get_service_charges())
    # except Exception as e:
    #     print(f"Error withdrawing service charges from SavingsAccount: {e}")
    # try:
    #     investment_new.withdraw(investment_new.get_service_charges())
    # except Exception as e:
    #     print(f"Error withdrawing service charges from InvestmentAccount (new): {e}")
    # try:
    #     investment_old.withdraw(investment_old.get_service_charges())
    # except Exception as e:
    #     print(f"Error withdrawing service charges from InvestmentAccount (old): {e}")

    # 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
    print(chequing)
    print(savings)
    print(investment_new)
    print(investment_old)

if __name__ == "__main__":
    main()