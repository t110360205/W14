import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Class.class_init import Ui_MainWindow 
from Class.work import working 
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    _translate = QtCore.QCoreApplication.translate
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    working(ui).wait()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()