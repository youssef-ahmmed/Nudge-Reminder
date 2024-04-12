import os

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout


class PathLoader(QWidget):
    def __init__(self):
        super().__init__()

        self.path_label = QLabel("File Name: ")
        self.load_button = QPushButton("Load")

        self.init_layout()

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.path_label)
        layout.addWidget(self.load_button)
        self.setLayout(layout)
