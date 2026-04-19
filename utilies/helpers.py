from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView


def fill_table(table, rows, headers):
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.setRowCount(len(rows))

    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            item = QTableWidgetItem(str(val) if val else "")
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            table.setItem(r, c, item)

    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def info(parent, msg):
    QMessageBox.information(parent, "Success", msg)


def err(parent, msg):
    QMessageBox.critical(parent, "Error", msg)