from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout


class ColumnDataNumbers(QWidget):
    def __init__(self):
        super().__init__()

        self.column_number_label = QLabel("Column Numbers:")

        self.name_label = QLabel("First Name:")
        self.name_edit = QLineEdit()
        self.phone_label = QLabel("Phone:")
        self.phone_edit = QLineEdit()
        self.msg_label = QLabel("Message:")
        self.msg_edit = QLineEdit()

        self.init_layout()
        self.validate_edit_line()

    def validate_edit_line(self):
        self.name_edit.setValidator(QIntValidator())
        self.phone_edit.setValidator(QIntValidator())
        self.msg_edit.setValidator(QIntValidator())

    def init_layout(self):
        section_layout = QVBoxLayout()
        
        data_layout = QHBoxLayout()
        data_layout.addWidget(self.name_label)
        data_layout.addWidget(self.name_edit)
        data_layout.addWidget(self.phone_label)
        data_layout.addWidget(self.phone_edit)
        data_layout.addWidget(self.msg_label)
        data_layout.addWidget(self.msg_edit)

        section_layout.addWidget(self.column_number_label)
        section_layout.addLayout(data_layout)

        self.setLayout(section_layout)
