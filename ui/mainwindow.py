import sys
import getpass
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MainWindow (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("NotifyMe")
        
        self.user_name = getpass.getuser()
        self.user_text = f"Hello {self.user_name}, welcome to NotifyMe!"
        
        self.text = QtWidgets.QLabel(f"Hello {self.user_name}", alignment=QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Get Started")
        self.start_button = QtWidgets.QPushButton("Start Timer")
        self.stop_button = QtWidgets.QPushButton("Stop Timer")
        self.settings_button = QtWidgets.QPushButton("Settings")

        self.top_buttons_layout = QtWidgets.QHBoxLayout()
        self.top_buttons_layout.addWidget(self.button)
        self.top_buttons_layout.addWidget(self.start_button)
        
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout()
        self.bottom_buttons_layout.addWidget(self.stop_button)
        self.bottom_buttons_layout.addWidget(self.settings_button)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        
        self.main_layout.addWidget(self.text)
        self.main_layout.addLayout(self.top_buttons_layout)
        self.main_layout.addLayout(self.bottom_buttons_layout)
        
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        if self.user_text:
            new_char = random.choice(self.user_text)
            self.text.setText(f"Random character: **{new_char}**")
        else:
            self.text.setText("Text is empty.")
