from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QFrame, QTabWidget, QStatusBar, QPushButton, QApplication
)
from PyQt5.QtCore import Qt

from ui.tabs.flights_tab import FlightsTab
from ui.tabs.passengers_tab import PassengersTab
from ui.tabs.bookings_tab import BookingsTab
from ui.tabs.payments_tab import PaymentsTab
from ui.tabs.schedule_tab import ScheduleTab
from utilies.style import LIGHT, DARK

from config.db import ORACLE_AVAILABLE


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._is_light = True          # start with the soft-light theme

        self.setWindowTitle("✈  Flight Booking System")
        self.setMinimumSize(960, 680)
        # self.setStyleSheet(LIGHT)

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(20, 16, 20, 10)
        root.setSpacing(12)

        # ── Header row ──────────────────────────────────────────────────────
        hdr_row = QHBoxLayout()

        hdr = QLabel("✈  Flight Booking System")
        hdr.setObjectName("heading")
        hdr_row.addWidget(hdr)

        hdr_row.addStretch()

        # Theme toggle button
        self.theme_btn = QPushButton("🌙  Dark")
        self.theme_btn.setObjectName("neutral")
        self.theme_btn.setFixedWidth(100)
        self.theme_btn.clicked.connect(self.toggle_theme)
        hdr_row.addWidget(self.theme_btn)

        root.addLayout(hdr_row)

        sub = QLabel("Airline Database  ·  KARMA Enterprises")
        sub.setObjectName("sub")
        root.addWidget(sub)

        div = QFrame()
        div.setObjectName("divider")
        root.addWidget(div)

        # ── Tabs ─────────────────────────────────────────────────────────────
        tabs = QTabWidget()
        tabs.addTab(FlightsTab(),    "  ✈  Flights  ")
        tabs.addTab(PassengersTab(), "  👤  Passengers  ")
        tabs.addTab(BookingsTab(),   "  🎫  Bookings  ")
        tabs.addTab(PaymentsTab(),   "  💳  Payments  ")
        tabs.addTab(ScheduleTab(),   "  📋  Schedule  ")
        root.addWidget(tabs)

        # ── Status bar ───────────────────────────────────────────────────────
        status = QStatusBar()
        self.setStatusBar(status)
        db_ok = "🟢  oracledb ready" if ORACLE_AVAILABLE else "🔴  oracledb not installed — run: pip install oracledb"
        status.showMessage(f"{db_ok}   |   Connected as: system @ localhost:1521/XE")

    # ─────────────────────────────────────────────────────────────────────────
    def toggle_theme(self):
        self._is_light = not self._is_light
        if self._is_light:
            QApplication.instance().setStyleSheet(LIGHT)
            self.theme_btn.setText("🌙  Dark")
        else:
            QApplication.instance().setStyleSheet(DARK)
            self.theme_btn.setText("☀️  Light")