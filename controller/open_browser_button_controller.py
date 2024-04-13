from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from alright import WhatsApp
from selenium import webdriver

import log_messages
from controller.log_controller import LogController
from core.input_validations import validate_inputs


class BrowserWorker(QObject):
    finished = pyqtSignal(WhatsApp)

    def run(self):
        browser = webdriver.Chrome()
        messenger = WhatsApp(browser)
        self.finished.emit(messenger)


class OpenBrowserButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(open_browser_button: QPushButton = None):
        if OpenBrowserButtonController._instance is None:
            OpenBrowserButtonController._instance = OpenBrowserButtonController(open_browser_button)
        return OpenBrowserButtonController._instance

    def __init__(self, open_browser_button: QPushButton):
        super(OpenBrowserButtonController, self).__init__()

        if OpenBrowserButtonController._instance is not None:
            raise Exception("An instance of OpenBrowserButtonController already exists. "
                            "Use get_instance() to access it.")

        self.open_browser_button = open_browser_button
        self.messenger = None
        self.worker = None

        self.start_communication()

    def start_communication(self):
        self.open_browser_button.clicked.connect(self._create_chrome_browser_instance)

    def _create_chrome_browser_instance(self):
        if not validate_inputs():
            return

        LogController.get_instance().log_info(log_messages.WAIT_FOR_OPEN)

        self.thread = QThread()
        self.worker = BrowserWorker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self._on_browser_created)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        self.open_browser_button.setEnabled(False)
        self.thread.finished.connect(lambda: self.open_browser_button.setEnabled(True))
        self.worker.finished.connect(
            lambda: LogController.get_instance().log_info(log_messages.SCAN_QR_CODE)
        )

    def _on_browser_created(self, messenger):
        self.messenger = messenger

    def get_whatsapp_message_instance(self):
        if not self.messenger:
            self._create_chrome_browser_instance()
        return self.messenger
