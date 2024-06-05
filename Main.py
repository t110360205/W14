from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
import sys
import socket
app = QApplication([])
main_window = MainWidget()

main_window.setStyleSheet("background-image: url(easy.jpg);")

main_window.setFixedSize(650, 450)
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec())
