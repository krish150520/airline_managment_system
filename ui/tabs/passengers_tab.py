from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QGroupBox
from PyQt5.QtCore import Qt

from config.db import get_connection
from utilies.helpers import fill_table, info, err


class PassengersTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        grp = QGroupBox("Add Passenger")
        grid = QGridLayout(grp)
        grid.setSpacing(10)

        labels = ["Passenger ID", "Name", "Age", "Gender", "Phone"]
        self.p_fields = {}
        for i, lbl in enumerate(labels):
            grid.addWidget(QLabel(lbl), i, 0)
            le = QLineEdit()
            le.setPlaceholderText(lbl)
            grid.addWidget(le, i, 1)
            self.p_fields[lbl] = le

        add_btn = QPushButton("👤  Add Passenger")
        add_btn.setObjectName("success")
        add_btn.clicked.connect(self.add_passenger)
        grid.addWidget(add_btn, len(labels), 1)
        layout.addWidget(grp)

        ref_btn = QPushButton("⟳  Refresh")
        ref_btn.setObjectName("neutral")
        ref_btn.clicked.connect(self.load_passengers)
        layout.addWidget(ref_btn, alignment=Qt.AlignRight)

        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_passengers()

    def load_passengers(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM passengers")
            rows = cur.fetchall()
            cur.close(); conn.close()
            fill_table(self.table, rows,
                       ["Passenger ID", "Name", "Age", "Gender", "Phone"])
        except Exception as e:
            err(self, str(e))

    def add_passenger(self):
        vals = [f.text().strip() for f in self.p_fields.values()]
        if not all(vals):
            err(self, "Please fill all fields."); return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO passengers VALUES(:1,:2,:3,:4,:5)", vals)
            conn.commit(); cur.close(); conn.close()
            info(self, "Passenger added!")
            for f in self.p_fields.values(): f.clear()
            self.load_passengers()
        except Exception as e:
            err(self, str(e))
