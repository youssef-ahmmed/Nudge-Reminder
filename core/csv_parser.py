import csv

from controller.column_data_numbers_controller import ColumnDataNumbersController
from controller.path_loader_controller import PathLoaderController
from controller.start_end_rows_controller import StartEndRowsController


def count_lines_and_columns_in_csv():
    csv_file_path: str = PathLoaderController.get_instance().get_csv_file_path()

    with open(csv_file_path, 'r') as file:
        line_count = sum(1 for _ in file) - 1
        file.seek(0)

        first_line = next(file)
        column_count = len(first_line.split(','))

    return line_count, column_count


def parse_csv_rows():
    csv_file_path: str = PathLoaderController.get_instance().get_csv_file_path()
    name, phone, msg = ColumnDataNumbersController.get_instance().get_column_data_numbers().values()
    start, end = StartEndRowsController.get_instance().get_start_end_rows_data()

    start_row, end_row = int(start) - 1, int(end) - 1
    name_col, phone_col, msg_col = int(name) - 1, int(phone) - 1, int(msg) - 1

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for i, row in enumerate(csv_reader):
            if start_row <= i <= end_row:
                phone_number = row[phone_col] if row[phone_col].startswith('+') else f"+{row[phone_col]}"
                selected_row = [row[name_col], phone_number, row[msg_col]]
                yield selected_row
            elif i > end_row:
                break
