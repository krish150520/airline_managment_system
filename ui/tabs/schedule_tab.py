from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QGroupBox
from PyQt5.QtCore import Qt

from config.db import get_connection
from utilies.helpers import fill_table, info, err

class ScheduleTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        hdr = QLabel("Live Flight Schedule")
        hdr.setObjectName("heading")
        layout.addWidget(hdr)
        sub = QLabel("Pulled from the FLIGHT_SCHEDULE database view")
        sub.setObjectName("sub")
        layout.addWidget(sub)

        ref_btn = QPushButton("⟳  Refresh Schedule")
        ref_btn.setObjectName("neutral")
        ref_btn.clicked.connect(self.load)
        layout.addWidget(ref_btn, alignment=Qt.AlignRight)

        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load()

    def load(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM flight_schedule")
            rows = cur.fetchall()
            cur.close(); conn.close()
            fill_table(self.table, rows,
                       ["Flight ID", "Airline", "Source", "Destination"])
        except Exception as e:
            err(self, str(e))

