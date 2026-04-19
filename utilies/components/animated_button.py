from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QColor


class AnimatedButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self._color = QColor("#4caf82")

        self.anim = QPropertyAnimation(self, b"color", self)
        self.anim.setDuration(200)

        self.setStyleSheet(self.get_style(self._color))

    def get_style(self, color):
        return f"""
        QPushButton {{
            background-color: {color.name()};
            color: white;
            border-radius: 10px;
            padding: 8px 20px;
        }}
        """

    def enterEvent(self, event):
        self.animate_to(QColor("#3d9e72"))
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animate_to(QColor("#4caf82"))
        super().leaveEvent(event)

    def animate_to(self, target_color):
        self.anim.stop()
        self.anim.setStartValue(self._color)
        self.anim.setEndValue(target_color)
        self.anim.start()

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color
        self.setStyleSheet(self.get_style(color))

    color = pyqtProperty(QColor, getColor, setColor)