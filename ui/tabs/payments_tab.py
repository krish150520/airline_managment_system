from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QGroupBox,QComboBox
from PyQt5.QtCore import Qt

from config.db import get_connection
from utilies.helpers import fill_table, info, err


class PaymentsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        grp = QGroupBox("Make Payment")
        grid = QGridLayout(grp)
        grid.setSpacing(10)

        grid.addWidget(QLabel("Booking ID"), 0, 0)
        self.pay_booking = QLineEdit(); self.pay_booking.setPlaceholderText("e.g. 1001")
        grid.addWidget(self.pay_booking, 0, 1)

        grid.addWidget(QLabel("Amount (₹)"), 1, 0)
        self.pay_amount = QLineEdit(); self.pay_amount.setPlaceholderText("e.g. 5000")
        grid.addWidget(self.pay_amount, 1, 1)

        grid.addWidget(QLabel("Payment Method"), 2, 0)
        self.pay_method = QComboBox()
        self.pay_method.addItems(["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash"])
        grid.addWidget(self.pay_method, 2, 1)

        pay_btn = QPushButton("💳  Make Payment")
        pay_btn.setObjectName("success")
        pay_btn.clicked.connect(self.make_payment)
        grid.addWidget(pay_btn, 3, 1)
        layout.addWidget(grp)

        ref_btn = QPushButton("⟳  Refresh Payments")
        ref_btn.setObjectName("neutral")
        ref_btn.clicked.connect(self.load_payments)
        layout.addWidget(ref_btn, alignment=Qt.AlignRight)

        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_payments()

    def load_payments(self):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM payments")
            rows = cur.fetchall()
            cur.close(); conn.close()
            fill_table(self.table, rows,
                       ["Payment ID", "Booking ID", "Amount (₹)", "Method", "Payment Date"])
        except Exception as e:
            err(self, str(e))

    def make_payment(self):
        bid = self.pay_booking.text().strip()
        amt = self.pay_amount.text().strip()
        meth = self.pay_method.currentText()
        if not all([bid, amt]):
            err(self, "Fill all payment fields."); return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.callproc("make_payment", [int(bid), float(amt), meth])
            conn.commit(); cur.close(); conn.close()
            info(self, "Payment recorded!")
            self.pay_booking.clear(); self.pay_amount.clear()
            self.load_payments()
        except Exception as e:
            err(self, str(e))
