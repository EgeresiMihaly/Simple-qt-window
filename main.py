from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        # window config
        self.setWindowTitle("Registration Form")
        self.resize(400,0)

        # window content
        main_layout = QVBoxLayout(self)

        self.first_name_field = QLineEdit()
        self.first_name_field.setPlaceholderText("First Name")
        main_layout.addWidget(self.first_name_field)

        self.last_name_field = QLineEdit()
        self.last_name_field.setPlaceholderText("Last Name")
        main_layout.addWidget(self.last_name_field)

      





if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()
    app.exec()