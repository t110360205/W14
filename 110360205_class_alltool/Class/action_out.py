import sys
sys.path.append('Class')
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from class_init import Ui_MainWindow 

class action_out:
    def __init__(self,reg):
        self.reg=reg
        pass

    def combine_name(self,stu_dict):
        backdata={'name': stu_dict}
        return backdata
    
    def add(self,stu_dict):
        backdata=stu_dict
        print(backdata)
        return backdata
    def mod(self,stu_dict):
        backdata={"name":stu_dict["name"],"scores_dict":stu_dict["scores"]}
        print(backdata)
        return backdata   
    def show(self,stu_dict):
        backdata={}
        return backdata     
    
        

