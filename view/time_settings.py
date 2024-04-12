from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox, QTimeEdit


class TimeSetting(QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QLabel('Time:')
        self.time_edit = QTimeEdit()
        self.send_instantly_checkbox = QCheckBox('Send Instantly')

        self.init_layout()
        self.start_communication()

    def init_layout(self):
        self.setLayout(QHBoxLayout())

        self.layout().addWidget(self.time_label)
        self.layout().addWidget(self.time_edit)
        self.layout().addWidget(self.send_instantly_checkbox)

    def start_communication(self):
        self.send_instantly_checkbox.stateChanged.connect(self.handle_checkbox_state)

    def handle_checkbox_state(self, state):
        self.time_edit.setEnabled(not state)
