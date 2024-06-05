from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget
import pygame
from WorkWidgets.AddWidget import AddWidget
from WorkWidgets.DelWidget import DelWidget
from WorkWidgets.HelpWidget import HelpWidget
from SocketClient import SocketClient
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.WidgetComponents import LabelComponent
from WorkWidgets.WidgetComponents import ButtonComponent
from WorkWidgets.WidgetComponents import TableComponent

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QGridLayout()
        self.setWindowTitle("Student Management System")
        self.student_info=ShowStuWidget()
        menu_widget = MenuWidget()
        menu_widget.setStyleSheet("background-image:none;background-color:rgba(0, 0, 0, 0);")
        self.student_info.setStyleSheet("background-image:none;background-color:rgba(0, 0, 0, 0);")
        blank_widget = QWidget()
        blank_widget.setStyleSheet("background-image: url(background.jpg);")



        layout.addWidget(blank_widget,0,0,4,3)
        layout.addWidget(self.student_info, 0, 0, 4, 2)
        
        layout.addWidget(menu_widget, 0, 2, 3, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)
        layout.setRowStretch(3, 1)

        self.init_player()
        
        self.setLayout(layout)
        menu_widget.change_signal.connect(self.student_info_load_callback)
        menu_widget.exit_signal.connect(self.close)
        
    def student_info_load_callback(self):
        self.student_info.load()
        #print("RowCount:", self.student_info.rowCount())  # 确认行数
        name_lst = [self.student_info.verticalHeaderItem(i).text() for i in range(self.student_info.rowCount())]
        #print(f"name_lst:{name_lst}")
    

    def init_player(self):
        pygame.mixer.init()
        pygame.mixer.music.load("background.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 表示循环播放
class MenuWidget(QtWidgets.QWidget):
    change_signal=QtCore.pyqtSignal()
    exit_signal=QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setObjectName("menu_widget")

        layout = QtWidgets.QVBoxLayout()
        add_button = ButtonComponent("Add student")
        del_button = ButtonComponent("Del")
        help_button=ButtonComponent("Help")
        exit_button=ButtonComponent("Exit")
        # https://medium.com/seaniap/python-lambda-函式-7e86a56f1996
        add_button.clicked.connect(self.add_widget)
        del_button.clicked.connect(self.del_widget)
        help_button.clicked.connect(self.help_widget)
        exit_button.clicked.connect(self.exit_action)
        #show_button.clicked.connect(lambda: self.update_widget_callback("show"))

        layout.addWidget(help_button,stretch=1)
        layout.addWidget(add_button, stretch=1)
        layout.addWidget(del_button,stretch=1)
        layout.addWidget(exit_button,stretch=1)

        self.setLayout(layout)
    def add_widget(self):
        addwidget = AddWidget()
        #addwidget.setStyleSheet("background-image: url(background3.jpg); background-size: cover;background-repeat: no-repeat;")
        addwidget.setFixedSize(800, 500)
        addwidget.exec()  
        self.change_signal.emit() 
    def del_widget(self):
        delwidget=DelWidget()
        delwidget.setStyleSheet("background-image: url(background2.jpg);")
        delwidget.setFixedSize(500, 100)
        delwidget.exec()  
        self.change_signal.emit() 
    def help_widget(self):
        delwidget=HelpWidget()
        delwidget.setStyleSheet("background-image: url(background4.jpg);")
        delwidget.setFixedSize(500, 100)
        delwidget.exec()  
    def exit_action(self):
        host = "127.0.0.1"
        port = 20001
        client=SocketClient(host,port)
        client.send_command("exit","")
        self.exit_signal.emit()
