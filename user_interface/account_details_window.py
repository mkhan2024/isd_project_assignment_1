__author__ = "ACE Faculty"
__version__ = "1.4.0"
__credits__ = "Md Apurba Khan"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetailsWindow.

        Args:
            account: The bank account to be displayed.
        """
        super().__init__()
        if not isinstance(account, BankAccount):
            self.reject()
            return

        self.account = copy.copy(account)
        self.account_number_label.setText(self.account.account_number)
        self.balance_label.setText(f"${self.account.balance:,.2f}")

        # Connect signals to slots
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)

    @Slot()
    def on_apply_transaction(self):
        """Handle deposit or withdraw button clicks to process transactions.

        Attempts to process the transaction amount entered by the user, updates the balance,
        and shows an error message if the transaction fails.
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid transaction amount.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            transaction_type = "Deposit" if self.sender() == self.deposit_button else "Withdraw"
            if transaction_type == "Deposit":
                self.account.deposit(amount)
            else:
                self.account.withdraw(amount)

            self.balance_label.setText(f"${self.account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
        except ValueError as e:
            QMessageBox.warning(self, "Error", f"{transaction_type} Failed: {str(e)}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    @Slot()
    def on_exit(self):
        """Handle the exit button click to close the dialog."""
        self.close()