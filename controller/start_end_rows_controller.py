from PyQt5.QtCore import QObject

from view.start_end_rows import StartEndRows


class StartEndRowsController(QObject):
    _instance = None

    @staticmethod
    def get_instance(start_end_rows: StartEndRows = None):
        if StartEndRowsController._instance is None:
            StartEndRowsController._instance = StartEndRowsController(start_end_rows)
        return StartEndRowsController._instance

    def __init__(self, start_end_rows: StartEndRows):
        super(StartEndRowsController, self).__init__()

        if StartEndRowsController._instance is not None:
            raise Exception("An instance of StartEndRowsController already exists. "
                            "Use get_instance() to access it.")

        self.start_row_edit = start_end_rows.start_edit
        self.end_row_edit = start_end_rows.end_edit

    def get_start_end_rows_data(self) -> list[int]:
        return [
            self.start_row_edit.text(),
            self.end_row_edit.text()
        ]
