from PyQt5.QtWidgets import (
     QWidget, QPushButton,
    QFileDialog, QLineEdit, QComboBox, QMessageBox, QFormLayout, QHBoxLayout,QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from util.source import SourceOptions

class GuiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Channel Order Validator")
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
        self.dvbt_input = QLineEdit()
        self.dvbt_input.setReadOnly(True)
        self.dvbt_input.setFixedWidth(field_width)
        self.dvbt_button = QPushButton("Browse")
        self.dvbt_button.setFixedWidth(button_width)
        self.dvbt_button.clicked.connect(self.browse_file1)
        dvbt_row = QHBoxLayout()
        dvbt_row.addWidget(self.dvbt_input)
        dvbt_row.addWidget(self.dvbt_button)
        layout.addRow("Upload DVBT File:", dvbt_row)

        # File 2 input
        self.file2_input = QLineEdit()
        self.file2_input.setReadOnly(True)
        self.file2_input.setFixedWidth(field_width)
        self.file2_button = QPushButton("Browse")
        self.file2_button.setFixedWidth(button_width)
        self.file2_button.clicked.connect(self.browse_file2)
        file2_row = QHBoxLayout()
        file2_row.addWidget(self.file2_input)
        file2_row.addWidget(self.file2_button)
        layout.addRow("Upload File 2:", file2_row)

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
        file_name, _ = QFileDialog.getOpenFileName(self, "Select DVBT File")
        if file_name:
            self.dvbt_input.setText(file_name)

    def browse_file2(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File 2")
        if file_name:
            self.file2_input.setText(file_name)

    def submit_files(self):
        file1 = self.dvbt_input.text()
        file2 = self.file2_input.text()
        selected_option = self.dropdown.currentText()

        if file1 and file2:
            QMessageBox.information(
                self,
                "Validation Result",
                f"Files validated successfully!\n\n"
                f"File 1: {file1}\n"
                f"File 2: {file2}\n"
                f"Channel Source: {selected_option}"
            )
        else:
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please upload both files and select a channel source."
            )