from PySide6.QtWidgets import QWidget, QApplication
import sys


app = QApplication(sys.argv)
my_window = QWidget()
my_window.setWindowTitle("My first Window")
my_window.resize(1200, 900)
my_window.show()
app.exec()
