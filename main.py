from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from ui.mainwindow import MainWindow
import sys

def main():
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

