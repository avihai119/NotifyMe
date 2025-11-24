import getpass
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.user_name = getpass.getuser()
        self.hello = f"Hello {self.user_name}"
        self.button = QtWidgets.QPushButton("Get Started")
        self.text = QtWidgets.QLabel(self.hello,
                                     alignment=QtCore.Qt.AlignCenter)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
