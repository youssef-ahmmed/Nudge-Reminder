from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QAbstractItemView, QLabel, QVBoxLayout


class StartEndRowsTableDisplay(QWidget):
    def __init__(self):
        super().__init__()

        self.table_label = QLabel("Start & End data:")
        self.table = QTableWidget(2, 3)

        self.init_layout()
        self.organize_table_headers()

    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.table_label)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def organize_table_headers(self):
        self.table.setHorizontalHeaderLabels(["Row No.", "Name", "Phone Number"])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(True)
