from PyQt5.QtGui import QColor, QTextCharFormat, QTextCursor

import log_messages
from view.log_widget import LogWidget


class LogController:
    _instance = None

    @staticmethod
    def get_instance(log_widget: LogWidget = None):
        if LogController._instance is None:
            LogController._instance = LogController(log_widget)
        return LogController._instance

    def __init__(self, log_widget: LogWidget):
        super(LogController, self).__init__()

        if LogController._instance is not None:
            raise Exception("An instance of LogController already exists. "
                            "Use get_instance() to access it.")

        self.log_widget = log_widget.log

    def log_error(self, message):
        self._log_message(f"[ERROR]: {message}", QColor(255, 0, 0))

    def log_success(self, message):
        self._log_message(f"[SUCCESS]: {message}", QColor(0, 128, 0))

    def log_info(self, message):
        self._log_message(f"[INFO]: {message}", QColor(0, 0, 255))

    def _log_message(self, message, color):
        cursor = self.log_widget.textCursor()
        cursor.movePosition(QTextCursor.End)

        format_msg = QTextCharFormat()
        format_msg.setForeground(color)

        cursor.insertText(message + "\n", format_msg)

        self.log_widget.setTextCursor(cursor)
        self.log_widget.ensureCursorVisible()

    def get_log_status(self):
        cursor = self.log_widget.log.textCursor()
        cursor.movePosition(QTextCursor.End - 1)
        cursor.select(QTextCursor.LineUnderCursor)
        return cursor.selectedText().strip()
