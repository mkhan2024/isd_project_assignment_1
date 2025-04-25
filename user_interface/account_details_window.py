__author__ = "ACE Faculty"
__version__ = "1.5.0"
__credits__ = "Md Apurba Khan"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
from user_interface.manage_data import update_data
import copy

class AccountDetailsWindow(DetailsWindow):
    """A dialog for displaying account details and performing bank account transactions.

    This class extends DetailsWindow to provide functionality for viewing an account's details
    and processing deposits or withdrawals. It emits a signal when the balance is updated.

    Attributes:
        balance_updated (Signal): Signal emitted when the account balance is updated.
        __account (BankAccount): The bank account being displayed and modified.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """Initializes the AccountDetailsWindow with the given bank account.

        Args:
            account (BankAccount): The bank account to display and process transactions for.

        Returns:
            None: If the account is invalid, the dialog is rejected.
        """
        super().__init__()
        if not isinstance(account, BankAccount):
            self.reject()
            return

        self.__account = copy.copy(account)
        self.account_number_label.setText(self.__account.account_number)
        self.balance_label.setText(f"${self.__account.balance:,.2f}")

        # Connect signals to slots
        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self):
        """Handles deposit or withdraw button clicks to process transactions.

        Attempts to process the transaction amount entered by the user, updates the balance,
        and emits the balance_updated signal. Shows an error message if the transaction fails.

        Raises:
            ValueError: If the transaction amount is not a valid number.
            Exception: If the transaction fails due to account restrictions (e.g., insufficient funds).
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.information(self, "Invalid Data", "Amount MUST be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            transaction_type = "Deposit" if self.sender() == self.deposit_button else "Withdraw"
            if transaction_type == "Deposit":
                self.__account.deposit(amount)
            else:
                self.__account.withdraw(amount)

            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            update_data(self.__account)  # Update accounts.csv
            self.balance_updated.emit(self.__account)  # Emit signal to refresh table
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            QMessageBox.information(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    @Slot()
    def __on_exit(self):
        """Handles the exit button click to close the dialog."""
        self.close()