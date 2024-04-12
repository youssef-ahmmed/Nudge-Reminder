from PyQt5.QtCore import QObject

from view.start_end_rows_table_display import StartEndRowsTableDisplay


class StartEndRowsTableDisplayController(QObject):
    _instance = None

    @staticmethod
    def get_instance(start_end_rows_table_display: StartEndRowsTableDisplay = None):
        if StartEndRowsTableDisplayController._instance is None:
            StartEndRowsTableDisplayController._instance = (
                StartEndRowsTableDisplayController(start_end_rows_table_display)
            )
        return StartEndRowsTableDisplayController._instance

    def __init__(self, start_end_rows_table_display: StartEndRowsTableDisplay):
        super(StartEndRowsTableDisplayController, self).__init__()

        if StartEndRowsTableDisplayController._instance is not None:
            raise Exception("An instance of StartEndRowsTableDisplayController already exists. "
                            "Use get_instance() to access it.")


