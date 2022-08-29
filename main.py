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
        # first Name
        self.first_name_field = QLineEdit()
        self.first_name_field.setPlaceholderText("First Name")
        main_layout.addWidget(self.first_name_field)
        #last name
        self.last_name_field = QLineEdit()
        self.last_name_field.setPlaceholderText("Last Name")
        main_layout.addWidget(self.last_name_field)
        # Phone number
        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("Phone")
        main_layout.addWidget(self.phone_field)
        #Address
        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("Address")
        main_layout.addWidget(self.address_field)
        #email
        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Email")
        main_layout.addWidget(self.email_field)

        save_button = QPushButton("Save")
        main_layout.addWidget(save_button)

        #connect signals/ slot mechanism

        save_button.clicked.connect(self.save_action)
        self.first_name_field.textChanged.connect(self.first_name_changed)

    def save_action(self):
        data_dictionary = {
            "first_name": self.first_name_field.text(),
            "last_name": self.last_name_field.text(),
            "phone": self.phone_field.text(),
            "email": self.email_field.text(),
            "address": self.address_field.text()
        }


    def first_name_changed(self,value):
        print(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()
    app.exec()