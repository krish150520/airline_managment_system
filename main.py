import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from utilies.style import LIGHT,DARK

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(LIGHT)

    win = MainWindow()
    win.show()
    
    sys.exit(app.exec_())