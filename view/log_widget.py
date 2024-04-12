from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextOption
from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QVBoxLayout, QDesktopWidget


class LogWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.log = QPlainTextEdit()

        self.init_ui()
        self.set_initial_style()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.log.setReadOnly(True)

        self.log.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.log.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

        self.layout().addWidget(self.log)

    def set_initial_style(self):
        self.log.setFont(QFont("Helvetica", 11, weight=QFont.Bold))
        self.log.setStyleSheet(
            "color: #333; background-color: #ADC4CE; border: 1px solid #AAA;"
        )

        self.setStyleSheet("border: 1px solid #AAA;")
