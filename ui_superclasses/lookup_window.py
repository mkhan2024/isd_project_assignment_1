__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Md Apurba Khan"

from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class LookupWindow(QMainWindow):
    """Base class for lookup windows in the PiXELL-River Financial System.

    This class provides the UI setup for looking up client details and displaying their bank accounts.
    It includes widgets for entering a client number, displaying client information, listing accounts
    in a table, and filtering the table based on user-defined criteria.

    Attributes:
        prompt_label (QLabel): Label prompting the user to enter a client number.
        client_number_edit (QLineEdit): Text field for entering the client number.
        lookup_button (QPushButton): Button to trigger the client lookup.
        client_info_label (QLabel): Label displaying the client's name.
        account_table (QTableWidget): Table displaying the client's bank accounts.
        filter_label (QLabel): Label indicating the filter state.
        filter_combo_box (QComboBox): Combo box for selecting the filter column.
        filter_edit (QLineEdit): Text field for entering the filter text.
        filter_button (QPushButton): Button to apply or reset the filter.
    """

    def __init__(self):
        """Initializes the LookupWindow by setting up the UI widgets and layout."""
        super().__init__()

        COLUMN_HEADERS = ["Account Number", "Balance", "Date Created", "Account Type"]

        self.setWindowTitle("Client Lookup")
        self.resize(600, 400)

        # Main layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QGridLayout(centralWidget)

        # Bold font for labels and headers
        bold_font = QFont()
        bold_font.setBold(True)

        # Widgets
        self.prompt_label = QLabel("Enter Client Number:")
        self.prompt_label.setFont(bold_font)
        self.client_number_edit = QLineEdit()
        self.lookup_button = QPushButton("Lookup Client")
        self.lookup_button.setDefault(True)

        self.client_info_label = QLabel()
        self.account_table = QTableWidget()
        self.prompt_label.setAlignment(Qt.AlignCenter)
        self.client_number_edit.setAlignment(Qt.AlignCenter)
        self.client_info_label.setAlignment(Qt.AlignCenter)

        # Assignment 5 Widgets
        self.filter_label = QLabel("Data is Not Currently Filtered")
        self.filter_label.setFont(bold_font)
        self.filter_edit = QLineEdit()
        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItems(COLUMN_HEADERS)
        self.filter_button = QPushButton("Apply Filter")

        # Adjusting layout to make widgets centered in the middle column of a 3-column layout
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(2, 1)

        # Add widgets to the layout, placing them in the second (middle) column
        layout.addWidget(self.prompt_label, 0, 1)
        layout.addWidget(self.client_number_edit, 1, 1)
        layout.addWidget(self.lookup_button, 2, 1)
        layout.addWidget(self.client_info_label, 3, 1)

        # Table (for BankAccount data) spans all columns
        layout.addWidget(self.account_table, 4, 0, 1, 3)

        # Add Assignment 5 Widgets
        layout.addWidget(self.filter_label, 5, 0)
        layout.addWidget(self.filter_combo_box, 6, 0)
        layout.addWidget(self.filter_edit, 6, 1)
        layout.addWidget(self.filter_button, 6, 2)

        self.account_table.setColumnCount(4)
        self.account_table.setHorizontalHeaderLabels(COLUMN_HEADERS)
        self.account_table.horizontalHeader().setFont(bold_font)
        self.account_table.resizeColumnsToContents()
        self.account_table.resizeRowsToContents()
        self.reset_display()

    def reset_display(self):
        """Resets the display by clearing fields and disabling filter widgets.

        Clears the contents of `client_number_edit`, `client_info_label`, `account_table`,
        and filter-related widgets, then sets focus to `client_info_label`.
        """
        self.account_table.setRowCount(0)
        self.client_number_edit.clear()
        self.client_info_label.setText("")
        self.client_info_label.setFocus()
        self.filter_edit.setText("")
        self.filter_combo_box.setCurrentIndex(0)
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_button.setEnabled(False)
        self.filter_label.setEnabled(False)