from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QGroupBox
from PyQt5.QtCore import Qt

from config.db import get_connection
from utilies.helpers import fill_table, info, err


class FlightsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        grp = QGroupBox("Add New Flight")
        grid = QGridLayout(grp)
        grid.setSpacing(10)

        labels = ["Flight ID", "Airline", "Source", "Destination",
                  "Departure (DD-MON-YYYY HH24:MI)", "Arrival (DD-MON-YYYY HH24:MI)", "Total Seats"]
        self.f_fields = {}
        for i, lbl in enumerate(labels):
            grid.addWidget(QLabel(lbl), i, 0)
            le = QLineEdit()
            le.setPlaceholderText(lbl)
            grid.addWidget(le, i, 1)
            self.f_fields[lbl] = le

        add_btn = QPushButton("✈  Add Flight")
        add_btn.setObjectName("success")
        add_btn.clicked.connect(self.add_flight)
        grid.addWidget(add_btn, len(labels), 1)
        layout.addWidget(grp)

        ref_btn = QPushButton("⟳  Refresh")
        ref_btn.setObjectName("neutral")
        ref_btn.clicked.connect(self.load_flights)
        layout.addWidget(ref_btn, alignment=Qt.AlignRight)

        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_flights()

    def load_flights(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM flights")
            rows = cur.fetchall()
            cur.close(); conn.close()
            fill_table(self.table, rows,
                       ["Flight ID", "Airline", "Source", "Destination",
                        "Departure", "Arrival", "Total Seats"])
        except Exception as e:
            err(self, str(e))

    def add_flight(self):
        vals = [f.text().strip() for f in self.f_fields.values()]
        if not all(vals):
            err(self, "Please fill all fields."); return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO flights VALUES(
                  :1,:2,:3,:4,
                  TO_DATE(:5,'DD-MON-YYYY HH24:MI'),
                  TO_DATE(:6,'DD-MON-YYYY HH24:MI'),
                  :7)
            """, vals)
            conn.commit(); cur.close(); conn.close()
            info(self, "Flight added successfully!")
            for f in self.f_fields.values(): f.clear()
            self.load_flights()
        except Exception as e:
            err(self, str(e))
