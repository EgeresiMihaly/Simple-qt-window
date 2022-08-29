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


        save_button = QPushButton("Save")
        main_layout.addWidget(save_button)

        #connect signals/ slot mechanism

        save_button.clicked.connect(self.save_action)
        self.first_name_field.textChanged.connect(self.first_name_changed)

    def save_action(self):
        print(f"First name: {self.first_name_field.text()}")
        print(f"Last name: {self.last_name_field.text()}")

    def first_name_changed(self,value):
        print(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()
    app.exec()