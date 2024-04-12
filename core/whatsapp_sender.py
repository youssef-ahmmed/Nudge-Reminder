from time import sleep

import pywhatkit
from pywhatkit.core.exceptions import CountryCodeException, InternetException, CallTimeException

from controller.log_controller import LogController


def send_multiple_instant_messages(data: list[list]):
    print('received data', data)
    for row in data:
        print(row)
        # try:
        pywhatkit.sendwhatmsg_instantly(row[1], row[2], 15, True, 3)
        sleep(1)
        # except (CountryCodeException, InternetException, CallTimeException) as e:
        #     LogController.get_instance().log_error(e)
        # except Exception as e:
        #     print(e)


def send_multiple_messages_at_time(data: list[list]):
    ...


def send_one_message_at_time(phone_number: str, message: str, hour: int, minutes: int):
    pywhatkit.sendwhatmsg(phone_number, message, hour, minutes)
