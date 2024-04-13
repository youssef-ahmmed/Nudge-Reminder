from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from controller.open_browser_button_controller import OpenBrowserButtonController


class OpenBrowserButton(QWidget):
    def __init__(self):
        super().__init__()

        self.open_browser_button = QPushButton("Open Chrom Browser")

        OpenBrowserButtonController.get_instance(self.open_browser_button)

        self.init_layout()

    def init_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.open_browser_button)
        self.setLayout(layout)
