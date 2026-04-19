from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QGroupBox
from PyQt5.QtCore import Qt

from config.db import get_connection
from utilies.helpers import fill_table, info, err
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QComboBox,
    QTableWidget, QTableWidgetItem, QMessageBox,
    QGroupBox, QStatusBar, QHeaderView, QFrame
)


class BookingsTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        row_layout = QHBoxLayout()

        # ── Book ──
        book_grp = QGroupBox("Book Ticket")
        bg = QGridLayout(book_grp)
        bg.setSpacing(10)

        bg.addWidget(QLabel("Passenger ID"), 0, 0)
        self.b_passenger = QLineEdit(); self.b_passenger.setPlaceholderText("e.g. 1")
        bg.addWidget(self.b_passenger, 0, 1)

        bg.addWidget(QLabel("Flight ID"), 1, 0)
        self.b_flight = QLineEdit(); self.b_flight.setPlaceholderText("e.g. 101")
        bg.addWidget(self.b_flight, 1, 1)

        bg.addWidget(QLabel("Seat Number"), 2, 0)
        self.b_seat = QLineEdit(); self.b_seat.setPlaceholderText("e.g. 12")
        bg.addWidget(self.b_seat, 2, 1)

        book_btn = QPushButton("🎫  Book Ticket")
        book_btn.setObjectName("success")
        book_btn.clicked.connect(self.book_ticket)
        bg.addWidget(book_btn, 3, 0, 1, 2)
        row_layout.addWidget(book_grp)

        # ── Cancel ──
        cancel_grp = QGroupBox("Cancel Ticket")
        cg = QGridLayout(cancel_grp)
        cg.setSpacing(10)

        cg.addWidget(QLabel("Booking ID"), 0, 0)
        self.c_booking = QLineEdit(); self.c_booking.setPlaceholderText("e.g. 1001")
        cg.addWidget(self.c_booking, 0, 1)

        cancel_btn = QPushButton("✖  Cancel Ticket")
        cancel_btn.setObjectName("danger")
        cancel_btn.clicked.connect(self.cancel_ticket)
        cg.addWidget(cancel_btn, 1, 0, 1, 2)
        row_layout.addWidget(cancel_grp)

        layout.addLayout(row_layout)

        ref_btn = QPushButton("⟳  Refresh Bookings")
        ref_btn.setObjectName("neutral")
        ref_btn.clicked.connect(self.load_bookings)
        layout.addWidget(ref_btn, alignment=Qt.AlignRight)

        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_bookings()

    def load_bookings(self):
         try:
             conn = get_connection()
             cur = conn.cursor()
             cur.execute("""
                 SELECT booking_id, passenger_id, flight_id, seat_number, booking_date
                 FROM bookings
                 WHERE status IS NULL OR status != 'CANCELLED'
             """)
             rows = cur.fetchall()
             cur.close(); conn.close()
             fill_table(self.table, rows,
                        ["Booking ID", "Passenger ID", "Flight ID", "Seat No.", "Booking Date"])
         except Exception as e:
             err(self, str(e))
    def book_ticket(self):
        p = self.b_passenger.text().strip()
        f = self.b_flight.text().strip()
        s = self.b_seat.text().strip()
        if not all([p, f, s]):
            err(self, "Fill all booking fields."); return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.callproc("book_ticket", [int(p), int(f), int(s)])
            conn.commit(); cur.close(); conn.close()
            info(self, "Ticket booked!")
            self.b_passenger.clear(); self.b_flight.clear(); self.b_seat.clear()
            self.load_bookings()
        except Exception as e:
            err(self, str(e))

    def cancel_ticket(self):
        bid = self.c_booking.text().strip()
        if not bid:
            err(self, "Enter Booking ID."); return
        reply = QMessageBox.question(self, "Confirm", f"Cancel booking {bid}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes: return
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.callproc("CANCEL_TICKET", [int(bid)])
            conn.commit(); cur.close(); conn.close()
            info(self, "Booking cancelled.")
            self.c_booking.clear()
            self.load_bookings()
        except Exception as e:
            err(self, str(e))
