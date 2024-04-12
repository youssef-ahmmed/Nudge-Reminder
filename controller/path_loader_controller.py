import os

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog

from view.path_loader import PathLoader


class PathLoaderController(QObject):
    _instance = None

    @staticmethod
    def get_instance(path_loader: PathLoader = None):
        if PathLoaderController._instance is None:
            PathLoaderController._instance = PathLoaderController(path_loader)
        return PathLoaderController._instance

    def __init__(self, path_loader: PathLoader):
        super(PathLoaderController, self).__init__()

        if PathLoaderController._instance is not None:
            raise Exception("An instance of PathLoaderController already exists. "
                            "Use get_instance() to access it.")

        self.file_name = None
        self.load_button = path_loader.load_button
        self.path_label = path_loader.path_label

        self.start_communication()

    def start_communication(self):
        self.load_button.clicked.connect(lambda: self.open_file_dialog())

    def open_file_dialog(self):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(
            self.load_button, "Open CSV File", "", "CSV Files (*.csv)", options=options
        )

        if self.file_name:
            self.path_label.setText(f"File Name: {os.path.basename(self.file_name)}")

    def get_csv_file_path(self):
        return self.file_name
