from PyQt5.QtCore import QObject

from view.time_settings import TimeSetting


class TimeSettingController(QObject):
    _instance = None

    @staticmethod
    def get_instance(time_setting: TimeSetting = None):
        if TimeSettingController._instance is None:
            TimeSettingController._instance = TimeSettingController(time_setting)
        return TimeSettingController._instance

    def __init__(self, time_setting: TimeSetting):
        super(TimeSettingController, self).__init__()

        if TimeSettingController._instance is not None:
            raise Exception("An instance of TimeSettingController already exists. "
                            "Use get_instance() to access it.")

        self.time_edit = time_setting.time_edit
        self.send_instantly_checkbox = time_setting.send_instantly_checkbox

    def get_checkbox_state(self):
        return self.send_instantly_checkbox.isChecked()

    def get_24h_time_format(self):
        selected_time = self.time_edit.time()
        hour = selected_time.hour()
        minute = selected_time.minute()

        return hour, minute
