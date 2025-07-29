from PyQt5.QtWidgets import (
     QWidget, QPushButton,
    QFileDialog, QLineEdit, QComboBox, QMessageBox, QFormLayout, QHBoxLayout,QSpacerItem, QSizePolicy
)
from services.formInputValidator import FormInputValidator
from services.sortorderValidator import SortOrderValidator
from util.source import SourceOptions

class GuiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Channel Order Validator:V1.0")
        self.setFixedSize(1000, 700)  # Prevent distortion on resize

        # Apply clean stylesheet
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
            }
            QPushButton {
                padding: 6px 12px;
                border-radius: 6px;
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLineEdit {
                padding: 4px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QComboBox {
                padding: 4px;
            }
        """)

        layout = QFormLayout()

        # Set consistent widths
        field_width = 400
        button_width = 100

        # DVBT File input
        self.dvbs_input = QLineEdit()
        self.dvbs_input.setReadOnly(True)
        self.dvbs_input.setFixedWidth(field_width)
        self.dvbt_button = QPushButton("Browse")
        self.dvbt_button.setFixedWidth(button_width)
        self.dvbt_button.clicked.connect(self.browse_file1)
        dvbt_row = QHBoxLayout()
        dvbt_row.addWidget(self.dvbs_input)
        dvbt_row.addWidget(self.dvbt_button)
        layout.addRow("Upload DVBS File(JSON):", dvbt_row)

        # File 2 input
        self.csv_input = QLineEdit()
        self.csv_input.setReadOnly(True)
        self.csv_input.setFixedWidth(field_width)
        self.file2_button = QPushButton("Browse")
        self.file2_button.setFixedWidth(button_width)
        self.file2_button.clicked.connect(self.browse_file2)
        file2_row = QHBoxLayout()
        file2_row.addWidget(self.csv_input)
        file2_row.addWidget(self.file2_button)
        layout.addRow("Upload Tv DB File(CSV):", file2_row)

        # Dropdown
        self.dropdown = QComboBox()
        self.dropdown.setFixedWidth(field_width)
        self.dropdown.addItems([option.value for option in SourceOptions])
        layout.addRow("Channel Source:", self.dropdown)

        # Add an empty row (spacer) before the Validate button
        spacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)  # This adds vertical space

        # Submit Button
        self.submit_button = QPushButton("Validate")
        self.submit_button.setFixedWidth(button_width)
        button_row = QHBoxLayout()
        button_row.addStretch()  # Add stretch before the button
        button_row.addWidget(self.submit_button)
        button_row.addStretch()  # Add stretch after the button
        
        layout.addRow(button_row)

        self.submit_button.clicked.connect(self.submit_files)
        self.setLayout(layout)

    def browse_file1(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select DVBS File")
        if file_name:
            self.dvbs_input.setText(file_name)

    def browse_file2(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Tv DB File")
        if file_name:
            self.csv_input.setText(file_name)

    def submit_files(self):
        dvbsFilePath = self.dvbs_input.text()
        dabFilePath = self.csv_input.text()
        selected_option_str = self.dropdown.currentText()

        is_valid, message, channel_source = FormInputValidator.validate(dvbsFilePath, dabFilePath, selected_option_str)

        if not is_valid:
            QMessageBox.critical(self, "Error", message)
            return

        is_pass, message = SortOrderValidator(channel_source, dabFilePath, dvbsFilePath).validate()
        if is_pass:
            QMessageBox.information(self, "Validation Result", message)
        else:
            QMessageBox.critical(self, "Validation Error", message)