__author__ = "ACE Faculty"
__version__ = "2.1.0"
__credits__ = "Md Apurba Khan"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot, Signal
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """A window for looking up client details and their bank accounts.

    Attributes:
        __client_listing (dict): Dictionary mapping client numbers to Client objects.
        __accounts (dict): Dictionary mapping account numbers to BankAccount objects.
    """

    def __init__(self):
        """Initialize the lookup window and connect events to handlers."""
        super().__init__()
        self.__client_listing, self.__accounts = load_data()

        # Connect signals to slots
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)  # Added for filtering

    @Slot()
    def __on_lookup_client(self):
        """Handle the lookup button click event to display client and account details.

        Fetches the client by number, displays their info, and lists their accounts in the table.
        Shows an error if the client number is invalid or not found.
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.information(self, "Input Error", "The client number must be numeric value.")
            self.reset_display()
            return

        if client_number not in self.__client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.")
            self.reset_display()
            return

        client = self.__client_listing[client_number]
        self.client_info_label.setText(f"{client.last_name}, {client.first_name}")

        self.account_table.setRowCount(0)
        for account in self.__accounts.values():
            if account.client_number == str(client_number):
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
                self.account_table.setItem(row, 0, QTableWidgetItem(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, QTableWidgetItem(str(account.date_created)))
                self.account_table.setItem(row, 3, QTableWidgetItem(account.__class__.__name__))
        self.account_table.resizeColumnsToContents()
        self.toggle_filter(False)  # Reset filter state after lookup

    @Slot()
    def __on_text_changed(self):
        """Handle text changes in the client number field by clearing the account table."""
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """Handle account table cell click to open the account details window.

        Args:
            row (int): The row of the clicked cell.
            column (int): The column of the clicked cell.
        """
        account_number_item = self.account_table.item(row, 0)
        if not account_number_item or not account_number_item.text():
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        account_number = account_number_item.text()
        if account_number not in self.__accounts:
            QMessageBox.information(self, "No Bank Account", "Bank Account selected DOES not exist.")
            return

        account = self.__accounts[account_number]
        details_window = AccountDetailsWindow(account)
        details_window.balance_updated.connect(self.__update_data)
        details_window.exec_()

    @Slot(BankAccount)
    def __update_data(self, account: BankAccount) -> None:
        """Updates the account table with the updated account data after a transaction.

        Args:
            account (BankAccount): The updated BankAccount object.
        """
        self.__accounts[account.account_number] = account
        client_number = int(self.client_number_edit.text())
        self.account_table.setRowCount(0)
        for acc in self.__accounts.values():
            if acc.client_number == str(client_number):
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
                self.account_table.setItem(row, 0, QTableWidgetItem(acc.account_number))
                balance_item = QTableWidgetItem(f"${acc.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, QTableWidgetItem(str(acc.date_created)))
                self.account_table.setItem(row, 3, QTableWidgetItem(acc.__class__.__name__))
        self.account_table.resizeColumnsToContents()

    @Slot()
    def __on_filter_clicked(self):
        """Handles the filter button click to apply or reset filtering on the account table."""
        if self.filter_button.text() == "Apply Filter":
            column_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().lower().strip()
            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, column_index)
                if item and filter_text in item.text().lower():
                    self.account_table.setRowHidden(row, False)  # Show matching rows
                else:
                    self.account_table.setRowHidden(row, True)  # Hide non-matching rows
            self.toggle_filter(True)
        else:
            self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool) -> None:
        """Toggles filter widgets to indicate filtering state.

        Args:
            filter_on (bool): True if filtering is active, False otherwise.
        """
        self.filter_button.setEnabled(True)
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
            self.filter_label.setText("Data is Not Currently Filtered")