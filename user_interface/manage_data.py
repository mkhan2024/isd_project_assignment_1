__author__ = "ACE Faculty"
__version__ = "1.0.1"
__credits__ = "Md Apurba Khan"

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from client.client import Client
from bank_account.bank_account import BankAccount

# GIVEN LOGGING AND FILE ACCESS CODE
root_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(root_dir, 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, 'manage_data.log')
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
data_dir = os.path.join(root_dir, 'data')
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
# END GIVEN LOGGING AND FILE ACCESS CODE

def load_data() -> tuple[dict, dict]:
    """Loads client and account data from CSV files into dictionaries.

    Reads client data from `clients.csv` and account data from `accounts.csv`, creating
    Client and BankAccount objects respectively. Logs errors if data is invalid or files
    are not found.

    Returns:
        tuple: A tuple of (client_listing, accounts) where:
            - client_listing (dict): Maps client_number (int) to Client objects.
            - accounts (dict): Maps account_number (str) to BankAccount objects.

    Raises:
        FileNotFoundError: If the CSV files are not found.
        ValueError: If data in the CSV files is invalid (e.g., non-numeric values).
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA
    try:
        with open(clients_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for record in reader:
                try:
                    client_number = int(record["client_number"])
                    first_name = record["first_name"].strip()
                    last_name = record["last_name"].strip()
                    email_address = record["email_address"].strip()

                    if not first_name:
                        raise ValueError("First Name cannot be blank")

                    client = Client(client_number, first_name, last_name, email_address)
                    client_listing[client_number] = client
                except ValueError as e:
                    logging.error(f"Unable to create client: {str(e)}")
                except Exception as e:
                    logging.error(f"Unable to create client: unexpected error - {str(e)}")
    except FileNotFoundError:
        logging.error(f"Client file {clients_csv_path} not found")

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for record in reader:
                try:
                    account_number = str(record["account_number"])
                    client_number = str(record["client_number"])
                    balance = float(record["balance"])
                    date_created = datetime.strptime(record["date_created"], "%Y-%m-%d").date()
                    account_type = record["account_type"]

                    if account_type == "ChequingAccount":
                        overdraft_limit = float(record["overdraft_limit"])
                        overdraft_rate = float(record["overdraft_rate"])
                        account = ChequingAccount(
                            account_number, client_number, balance, date_created,
                            overdraft_limit, overdraft_rate
                        )
                    elif account_type == "SavingsAccount":
                        minimum_balance = float(record["minimum_balance"])
                        account = SavingsAccount(
                            account_number, client_number, balance, date_created,
                            minimum_balance
                        )
                    elif account_type == "InvestmentAccount":
                        account = InvestmentAccount(
                            account_number, client_number, balance, date_created, 2.55
                        )
                    else:
                        raise ValueError("Not a valid account type")

                    if int(client_number) in client_listing:
                        accounts[account_number] = account
                    else:
                        logging.error(
                            f"Bank Account: {account_number} contains invalid client number {client_number}"
                        )
                except ValueError as e:
                    logging.error(f"Unable to create bank account: {str(e)}")
                except Exception as e:
                    logging.error(f"Unable to create bank account: unexpected error - {str(e)}")
    except FileNotFoundError:
        logging.error(f"Account file {accounts_csv_path} not found")

    return (client_listing, accounts)

def update_data(updated_account: BankAccount) -> None:
    """Updates the accounts.csv file with the balance from the given BankAccount.

    Args:
        updated_account (BankAccount): A bank account containing an updated balance.

    Raises:
        FileNotFoundError: If the accounts.csv file is not found.
        PermissionError: If there are permission issues writing to the file.
        Exception: For other unexpected errors during file writing.
    """
    updated_rows = []

    try:
        with open(accounts_csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            fields = reader.fieldnames
            
            for row in reader:
                # Keep account_number as string to match updated_account.account_number
                account_number = row['account_number']
                if account_number == updated_account.account_number:
                    row['balance'] = str(updated_account.balance)  # Convert to string for CSV
                updated_rows.append(row)

        with open(accounts_csv_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(updated_rows)
    except FileNotFoundError:
        logging.error(f"Unable to update accounts.csv: File {accounts_csv_path} not found")
    except PermissionError:
        logging.error(f"Unable to update accounts.csv: Permission denied")
    except Exception as e:
        logging.error(f"Unable to update accounts.csv: Unexpected error - {str(e)}")

# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients, accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == str(client.client_number):
                print(f"{account}\n")
        print("=========================================")