from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QPushButton

from controller.log_controller import LogController
from core.input_validations import validate_inputs
from core.whatsapp_sender import send_multiple_instant_messages


def send_messages():
    if not validate_inputs():
        return

    send_multiple_instant_messages()

    LogController.get_instance().log_success("All messages have been sent successfully")


class SendButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(send_button: QPushButton = None):
        if SendButtonController._instance is None:
            SendButtonController._instance = SendButtonController(send_button)
        return SendButtonController._instance

    def __init__(self, send_button: QPushButton):
        super(SendButtonController, self).__init__()

        if SendButtonController._instance is not None:
            raise Exception("An instance of SendButtonController already exists. "
                            "Use get_instance() to access it.")

        self.send_button = send_button

        self.start_communication()

    def start_communication(self):
        self.send_button.clicked.connect(send_messages)
