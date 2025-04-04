__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Md Apurba Khan"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """A window for looking up client details and their bank accounts."""

    def __init__(self):
        """Initialize the lookup window and connect events to handlers."""
        super().__init__()
        self.client_listing, self.accounts = load_data()

        # Connect signals to slots
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)

    @Slot()
    def on_lookup_client(self):
        """Handle the lookup button click event to display client and account details.

        Fetches the client by number, displays their info, and lists their accounts in the table.
        Shows an error if the client number is invalid or not found.
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid Client Number format.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Error", f"Client Number {client_number} not found.")
            self.reset_display()
            return

        client = self.client_listing[client_number]
        self.client_info_label.setText(f"{client.last_name}, {client.first_name}")

        self.account_table.setRowCount(0)
        for account in self.accounts.values():
            if account.client_number == str(client_number):
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
                self.account_table.setItem(row, 0, QTableWidgetItem(account.account_number))
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row, 2, QTableWidgetItem(str(account.date_created)))
                self.account_table.setItem(row, 3, QTableWidgetItem(account.__class__.__name__))
        self.account_table.resizeColumnsToContents()

    @Slot()
    def on_text_changed(self):
        """Handle text changes in the client number field by clearing the account table."""
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        """Handle account table cell click to open the account details window.

        Args:
            row (int): The row of the clicked cell.
            column (int): The column of the clicked cell.
        """
        account_number_item = self.account_table.item(row, 0)
        if not account_number_item or not account_number_item.text():
            QMessageBox.warning(self, "Error", "No account selected.")
            return

        account_number = account_number_item.text()
        if account_number not in self.accounts:
            QMessageBox.warning(self, "Error", f"Account Number {account_number} not found.")
            return

        account = self.accounts[account_number]
        details_window = AccountDetailsWindow(account)
        details_window.exec_()