from time import sleep

from controller.open_browser_button_controller import OpenBrowserButtonController
from core.csv_parser import parse_csv_rows


def send_multiple_instant_messages():
    messenger = OpenBrowserButtonController.get_instance().get_whatsapp_message_instance()

    for row in parse_csv_rows():
        messenger.send_direct_message(row[1], row[2], saved=False)
        sleep(3)
