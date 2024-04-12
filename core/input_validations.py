import log_messages
from controller.column_data_numbers_controller import ColumnDataNumbersController
from controller.path_loader_controller import PathLoaderController
from controller.start_end_rows_controller import StartEndRowsController
from core.csv_parser import count_lines_and_columns_in_csv


class InputValidationError(Exception):
    pass


class InputValidations:
    @staticmethod
    def validate_csv_file_exist():
        file_path = PathLoaderController.get_instance().get_csv_file_path()
        if not file_path:
            raise InputValidationError(log_messages.CSV_NOT_EXIST)

    @staticmethod
    def validate_start_end_rows():
        start, end = StartEndRowsController.get_instance().get_start_end_rows_data()

        if not start:
            raise InputValidationError(log_messages.START_ROW_ERROR)
        if not end:
            raise InputValidationError(log_messages.END_ROW_ERROR)

        start_row, end_row = int(start), int(end)

        if start_row >= end_row:
            raise InputValidationError(log_messages.START_BIGGER_THAN_END)

        csv_lines = count_lines_and_columns_in_csv()[0]
        if start_row >= csv_lines:
            raise InputValidationError(log_messages.START_BIGGER_THAN_LINE_COUNT)

        if end_row > csv_lines:
            raise InputValidationError(log_messages.END_BIGGER_THAN_LINE_COUNT)

    @staticmethod
    def validate_column_numbers():
        name, phone, msg = ColumnDataNumbersController.get_instance().get_column_data_numbers().values()

        if not name:
            raise InputValidationError(log_messages.NAME_COLUMN_ERROR)
        if not phone:
            raise InputValidationError(log_messages.PHONE_COLUMN_ERROR)
        if not msg:
            raise InputValidationError(log_messages.MESSAGE_COLUMN_ERROR)

        name_col, phone_col, msg_col = int(name), int(phone), int(msg)
        column_count = count_lines_and_columns_in_csv()[1]

        if name_col > column_count:
            raise InputValidationError(log_messages.NAME_COLUMN_BIGGER)
        if phone_col > column_count:
            raise InputValidationError(log_messages.PHONE_COLUMN_BIGGER)
        if msg_col > column_count:
            raise InputValidationError(log_messages.MESSAGE_COLUMN_BIGGER)
