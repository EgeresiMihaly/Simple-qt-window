from PySide6.QtWidgets import QWidget, QApplication
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()
    app.exec()