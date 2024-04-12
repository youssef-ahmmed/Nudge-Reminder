from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit


class StartEndRows(QWidget):
    def __init__(self):
        super().__init__()

        self.start_label = QLabel('Start Row:')
        self.start_edit = QLineEdit()
        self.end_label = QLabel('End Row:')
        self.end_edit = QLineEdit()

        self.init_layout()
        self.validate_edit_line()

    def validate_edit_line(self):
        self.start_edit.setValidator(QIntValidator())
        self.end_edit.setValidator(QIntValidator())

    def init_layout(self):
        self.setLayout(QHBoxLayout())

        self.layout().addWidget(self.start_label)
        self.layout().addWidget(self.start_edit)
        self.layout().addWidget(self.end_label)
        self.layout().addWidget(self.end_edit)
