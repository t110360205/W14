from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)
main_window = MainWidget()

main_window.setWindowTitle("Student Management System")
main_window.setFixedSize(700, 400)
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec())
