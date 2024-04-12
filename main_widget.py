import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDesktopWidget

from controller.column_data_numbers_controller import ColumnDataNumbersController
from controller.log_controller import LogController
from controller.path_loader_controller import PathLoaderController
from controller.start_end_rows_controller import StartEndRowsController
from controller.table_display_controller import StartEndRowsTableDisplayController
from controller.time_setting_controller import TimeSettingController
from view.column_data_numbers import ColumnDataNumbers
from view.log_widget import LogWidget
from view.path_loader import PathLoader
from view.send_button import SendButton
from view.start_end_rows import StartEndRows
from view.start_end_rows_table_display import StartEndRowsTableDisplay
from view.time_settings import TimeSetting


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.init_ui()
        self.create_controller()

        self.center_on_screen()

    def create_widgets(self):
        self.time_setting = TimeSetting()
        self.start_end_rows = StartEndRows()
        self.path_loader = PathLoader()
        self.column_data_numbers = ColumnDataNumbers()
        self.start_end_rows_table_display = StartEndRowsTableDisplay()
        self.send_button = SendButton()
        self.log_widget = LogWidget()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.time_setting)
        self.layout().addWidget(self.path_loader)
        self.layout().addWidget(self.start_end_rows)
        self.layout().addWidget(self.column_data_numbers)
        self.layout().addWidget(self.start_end_rows_table_display)
        self.layout().addWidget(self.send_button)
        self.layout().addWidget(self.log_widget)

        self.setWindowTitle("Nudge Reminder")
        self.show()

    def create_controller(self):
        TimeSettingController.get_instance(self.time_setting)
        PathLoaderController.get_instance(self.path_loader)
        StartEndRowsController.get_instance(self.start_end_rows)
        ColumnDataNumbersController.get_instance(self.column_data_numbers)
        StartEndRowsTableDisplayController.get_instance(self.start_end_rows_table_display)
        LogController.get_instance(self.log_widget)

    def center_on_screen(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        self.move(int((screen_geometry.width() - self.width()) / 2),
                  int((screen_geometry.height() - self.height()) / 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
