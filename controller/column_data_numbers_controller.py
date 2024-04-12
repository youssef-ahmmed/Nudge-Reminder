from PyQt5.QtCore import QObject

from view.column_data_numbers import ColumnDataNumbers


class ColumnDataNumbersController(QObject):
    _instance = None

    @staticmethod
    def get_instance(column_data_numbers: ColumnDataNumbers = None):
        if ColumnDataNumbersController._instance is None:
            ColumnDataNumbersController._instance = ColumnDataNumbersController(column_data_numbers)
        return ColumnDataNumbersController._instance

    def __init__(self, column_data_numbers: ColumnDataNumbers):
        super(ColumnDataNumbersController, self).__init__()

        if ColumnDataNumbersController._instance is not None:
            raise Exception("An instance of ColumnDataNumbersController already exists. "
                            "Use get_instance() to access it.")

        self.name_edit = column_data_numbers.name_edit
        self.phone_edit = column_data_numbers.phone_edit
        self.msg_edit = column_data_numbers.msg_edit

    def get_column_data_numbers(self) -> dict[str, int]:
        return {
            "name": self.name_edit.text(),
            "phone": self.phone_edit.text(),
            "msg": self.msg_edit.text()
        }
