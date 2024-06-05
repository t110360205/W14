from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication,QWidget
from PyQt6 import sip
import sys

app = QApplication([])

main_window = MainWidget()
#main_window.setStyleSheet("background: none;")
main_window.setStyleSheet("background-image: url(background.jpg);")
#background_widget = QWidget(main_window)
#background_widget.setStyleSheet("background-image: url(background.jpg);")


#main_window.setMinimumSize(800, 500)
main_window.setFixedSize(800, 500)
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec())
