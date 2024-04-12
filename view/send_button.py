from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from controller.send_button_controller import SendButtonController


class SendButton(QWidget):
    def __init__(self):
        super().__init__()

        self.send_button = QPushButton('Send Messages')

        SendButtonController.get_instance(self.send_button)

        self.init_layout()

    def init_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.send_button)
        self.setLayout(layout)
