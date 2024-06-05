from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent,RadioComponent,ComboboxComponent

from SocketClient import SocketClient
from PyQt6.QtCore import pyqtSignal
import json

class HelpWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("help_widget")
        self.setWindowTitle("Help")
        layout=QtWidgets.QGridLayout()

        self.message=LabelComponent(16,"add按鈕可以選擇增加學生或是某學生的科目\ndel可以刪除學生\n如果需要修改成績，直接點擊表格修改即可")
        self.message.setStyleSheet("color:black;font-weight: bold;")

        blank_widget = QWidget()
        blank_widget.setStyleSheet("background-image: url(background4.jpg);")

        layout.addWidget(blank_widget,0,0,1,1)
        layout.addWidget(self.message,0,0,1,1)


        self.setLayout(layout)

