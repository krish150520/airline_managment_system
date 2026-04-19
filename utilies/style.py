DARK = """
QMainWindow, QWidget {
    background-color: #0f1117;
    color: #e8eaf0;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}
QTabWidget::pane {
    border: 1px solid #2a2d3e;
    border-radius: 6px;
    background: #161a27;
}
QTabBar::tab {
    background: #1e2235;
    color: #7c82a0;
    padding: 10px 22px;
    border: none;
    margin-right: 2px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 0.5px;
}
QTabBar::tab:selected { background: #2563eb; color: #ffffff; }
QTabBar::tab:hover {
    background: #252a40;
    color: #c0c4d8;
}QGroupBox {
    border: 1px solid #2a2d3e;
    border-radius: 8px;
    margin-top: 14px;
    padding: 12px;
    background: #161a27;
    font-weight: 700;
    color: #7c8db5;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 6px; }
QLineEdit, QComboBox {
    background: #1e2235;
    border: 1px solid #2a2d3e;
    border-radius: 5px;
    padding: 7px 10px;
    color: #e8eaf0;
    selection-background-color: #2563eb;
}
QLineEdit:focus, QComboBox:focus { border: 1px solid #2563eb; }
QLineEdit::placeholder { color: #4a4f6a; }
QComboBox::drop-down { border: none; width: 24px; }
QComboBox::down-arrow { image: none; border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 6px solid #7c82a0; margin-right: 6px; }
QComboBox QAbstractItemView { background: #1e2235; border: 1px solid #2a2d3e; selection-background-color: #2563eb; color: #e8eaf0; }
QPushButton { background: #2563eb; color: #ffffff; border: none; border-radius: 5px; padding: 8px 20px; font-weight: 700; font-size: 12px; letter-spacing: 0.4px; }
QPushButton:hover { background: #3b74f0; }
QPushButton:pressed { background: #1a4fc4; }
QPushButton#danger { background: #dc2626; }
QPushButton#danger:hover { background: #ef4444; }
QPushButton#success { background: #16a34a; }
QPushButton#success:hover { background: #22c55e; }
QPushButton#neutral { background: #374151; }
QPushButton#neutral:hover { background: #4b5563; }
QTableWidget { background: #161a27; border: 1px solid #2a2d3e; border-radius: 6px; gridline-color: #1e2235; color: #e8eaf0; selection-background-color: #1e3a7a; }
QTableWidget::item { padding: 6px 10px; }
QHeaderView::section { background: #1e2235; color: #7c8db5; border: none; border-right: 1px solid #2a2d3e; padding: 8px 10px; font-weight: 700; font-size: 11px; letter-spacing: 0.8px; text-transform: uppercase; }
QStatusBar { background: #0f1117; color: #4a4f6a; border-top: 1px solid #2a2d3e; font-size: 11px; }
QLabel#heading { font-size: 22px; font-weight: 800; color: #e8eaf0; letter-spacing: -0.5px; }
QLabel#sub { font-size: 12px; color: #4a4f6a; }
QFrame#divider { background: #2a2d3e; max-height: 1px; }
"""

# ── Soft Light theme  (inspired by the reference UI image) ──────────────────
# Palette:
#   bg         #f0f2f0   very light warm-grey page background
#   surface    #ffffff   card / pane background
#   surface2   #f5f7f5   input / header background
#   border     #e2e6e2   subtle separator
#   accent     #4caf82   teal-green (matches the "Active" badge / map pin in img)
#   accent-h   #3d9e72   hover
#   accent-p   #2e8a5e   pressed
#   text       #1a2a22   near-black with green tint
#   muted      #7a8f82   placeholder / secondary text
#   danger     #e05c5c
#   success    #4caf82
#   neutral    #d0d8d2   light pill button
# ─────────────────────────────────────────────────────────────────────────────
LIGHT = """
QMainWindow, QWidget {
    background-color: #f0f2f0;
    color: #1a2a22;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}

/* ── Tab bar ── */
QTabWidget::pane {
    border: 1px solid #e2e6e2;
    border-radius: 12px;
    background: #ffffff;
}
QTabBar::tab {
    background: #e8ede9;
    color: #7a8f82;
    padding: 10px 24px;
    border: none;
    margin-right: 3px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 0.3px;
}
QTabBar::tab:selected {
    background: #4caf82;
    color: #ffffff;
}
QTabBar::tab:hover:!selected {
    background: #daeee3;
    color: #2e6e4e;
}

/* ── Group boxes (cards) ── */
QGroupBox {
    border: 1.5px solid #e2e6e2;
    border-radius: 14px;
    margin-top: 16px;
    padding: 14px;
    background: #ffffff;
    font-weight: 700;
    color: #7a8f82;
    font-size: 11px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 14px;
    padding: 0 6px;
    background: #ffffff;
    border-radius: 4px;
}

/* ── Inputs ── */
QLineEdit, QComboBox {
    background: #f5f7f5;
    border: 1.5px solid #e2e6e2;
    border-radius: 8px;
    padding: 8px 12px;
    color: #1a2a22;
    selection-background-color: #4caf82;
    selection-color: #ffffff;
}
QLineEdit:focus, QComboBox:focus {
    border: 1.5px solid #4caf82;
    background: #f0faf5;
}
QLineEdit::placeholder { color: #aabfb2; }
QComboBox::drop-down { border: none; width: 26px; }
QComboBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 6px solid #7a8f82;
    margin-right: 8px;
}
QComboBox QAbstractItemView {
    background: #ffffff;
    border: 1px solid #e2e6e2;
    border-radius: 8px;
    selection-background-color: #daeee3;
    selection-color: #1a2a22;
    color: #1a2a22;
    padding: 4px;
}

/* ── Buttons ── */
QPushButton {
    background: #4caf82;
    color: #ffffff;
    border: none;
    border-radius: 10px;
    padding: 9px 22px;
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 0.3px;
}
QPushButton:hover  { background: #3d9e72; }
QPushButton:pressed { background: #2e8a5e; }

QPushButton#danger {
    background: #fdecea;
    color: #c0392b;
    border: 1.5px solid #f5c6c2;
}
QPushButton#danger:hover { background: #fad5d0; color: #a93226; }

QPushButton#success {
    background: #4caf82;
    color: #ffffff;
}
QPushButton#success:hover { background: #3d9e72; }

QPushButton#neutral {
    background: #eaf0eb;
    color: #4a6a55;
    border: 1.5px solid #d0d8d2;
}
QPushButton#neutral:hover { background: #dce8de; color: #2e5040; }

/* ── Table ── */
QTableWidget {
    background: #ffffff;
    border: 1.5px solid #e2e6e2;
    border-radius: 12px;
    gridline-color: #f0f4f1;
    color: #1a2a22;
    selection-background-color: #daeee3;
    selection-color: #1a2a22;
    alternate-background-color: #f7faf8;
}
QTableWidget::item { padding: 7px 12px; border-radius: 4px; }
QTableWidget::item:selected { background: #daeee3; color: #1a2a22; }

QHeaderView::section {
    background: #f0f4f1;
    color: #7a8f82;
    border: none;
    border-right: 1px solid #e2e6e2;
    border-bottom: 1.5px solid #d0d8d2;
    padding: 9px 12px;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: 0.7px;
    text-transform: uppercase;
}
QHeaderView::section:first { border-top-left-radius: 10px; }
QHeaderView::section:last  { border-top-right-radius: 10px; border-right: none; }

/* ── Scroll bars ── */
QScrollBar:vertical {
    background: #f0f2f0;
    width: 8px;
    border-radius: 4px;
    margin: 0;
}
QScrollBar::handle:vertical {
    background: #c8d8cc;
    border-radius: 4px;
    min-height: 24px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
QScrollBar:horizontal {
    background: #f0f2f0;
    height: 8px;
    border-radius: 4px;
}
QScrollBar::handle:horizontal {
    background: #c8d8cc;
    border-radius: 4px;
    min-width: 24px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { width: 0; }

/* ── Status bar ── */
QStatusBar {
    background: #f0f2f0;
    color: #9ab0a0;
    border-top: 1px solid #e2e6e2;
    font-size: 11px;
    padding: 2px 8px;
}

/* ── Labels ── */
QLabel#heading {
    font-size: 22px;
    font-weight: 800;
    color: #1a2a22;
    letter-spacing: -0.5px;
}
QLabel#sub {
    font-size: 12px;
    color: #9ab0a0;
}
QFrame#divider {
    background: #e2e6e2;
    max-height: 1px;
}

/* ── Message boxes ── */
QMessageBox {
    background: #ffffff;
    color: #1a2a22;
}
QMessageBox QPushButton {
    min-width: 80px;
    padding: 7px 18px;
}
"""

# Default to LIGHT — change to DARK to switch
STYLE = LIGHT