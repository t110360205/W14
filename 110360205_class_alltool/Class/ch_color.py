import sys
sys.path.append('Class')
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from class_init import Ui_MainWindow 

class ch_color:
    def __init__(self,ui):
        self.ui=ui
    def color_init(self):
        
        '''self.ui.lab_title.setStyleSheet("QLabel { color: #900020; }") 
        self.ui.lab_addstu.setStyleSheet("QLabel { color: #900020; }")  
        self.ui.lab_name.setStyleSheet("QLabel { color: #900020; }")  
        self.ui.lab_sj.setStyleSheet("QLabel { color: #900020; }")  
        self.ui.lab_score.setStyleSheet("QLabel { color: #900020; }")  
        self.ui.lab_show.setStyleSheet("QLabel { color: #900020; }")  
        self.ui.lab_show_2.setStyleSheet("QLabel { color: #900020; }") 
        
        self.ui.cb_del.setStyleSheet("QComboBox { background-color: #F8AFA6; }")
        self.ui.lcdNumber.setStyleSheet("QLCDNumber { background-color: #F8AFA6; }")
        self.ui.lab_show_2.setStyleSheet("QLabel { background-color: #F8AFA6; }")
        self.ui.tx_show.setStyleSheet("QTextEdit { background-color: #F8AFA6; }")
        self.ui.txe_name.setStyleSheet("QTextEdit { background-color: #F8AFA6; }")
        self.ui.txe_sj.setStyleSheet("QTextEdit { background-color: #F8AFA6; }")
        self.ui.txe_score.setStyleSheet("QTextEdit { background-color: #F8AFA6; }")
        self.ui.pb_query.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_add.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_send.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_addstu.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_show.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_modify.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_del2.setStyleSheet("QPushButton { background-color: #F79489; }")
        self.ui.pb_del1.setStyleSheet("QPushButton { background-color: #F79489; }")'''
        self.ui.menubar.setStyleSheet("QMenuBar { background-color: #F79489; }")
        self.ui.centralwidget.setStyleSheet("QWidget { background-color: #FADCD9; } "
                                            "QLabel { color: #900020; }"
                                            "QMenuBar { background-color: #F79489; }"
                                            "QComboBox { background-color: #F8AFA6; }"
                                            "QTextEdit { background-color: #F8AFA6; }"
                                            "QPushButton { background-color: #F79489; }" 
                                                ) 