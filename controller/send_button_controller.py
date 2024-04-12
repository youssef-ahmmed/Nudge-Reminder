import threading

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QPushButton

from controller.log_controller import LogController
from controller.time_setting_controller import TimeSettingController
from core.csv_parser import parse_csv_to_list_of_lists
from core.input_validations import InputValidations, InputValidationError
from core.whatsapp_sender import send_multiple_instant_messages, send_multiple_messages_at_time


def validate_inputs() -> bool:
    try:
        InputValidations.validate_csv_file_exist()
        InputValidations.validate_start_end_rows()
        InputValidations.validate_column_numbers()

        return True
    except InputValidationError as e:
        LogController.get_instance().log_error(str(e))
        return False


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
        self.send_button.clicked.connect(self.send_messages)

    def send_messages(self):
        if not validate_inputs():
            return

        data = parse_csv_to_list_of_lists()
        print('data', data)
        is_send_now_checked = TimeSettingController.get_instance().get_checkbox_state()

        if is_send_now_checked:
            send_thread = threading.Thread(target=send_multiple_instant_messages, args=(data,))
            send_thread.start()

            send_thread.join()

            LogController.get_instance().log_success("All messages have been sent successfully")
