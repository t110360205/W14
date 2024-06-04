import sys
sys.path.append('Class')
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from class_init import Ui_MainWindow 

class action_in:
    def __init__(self,ui):
        self.ui=ui
    def display_save(self,result,sendreg):
        if result['status'] == "OK":
            self.ui.lab_show.setText(f"{self.ui.pb_add.text()} {sendreg} success")
            self.ui.pb_query.setEnabled(True)
            self.ui.txe_name.setEnabled(True)
            self.ui.txe_sj.setEnabled(False)
            self.ui.pb_add.setEnabled(False)
            self.ui.txe_score.setEnabled(False)
            self.ui.pb_send.setEnabled(False)
            self.ui.txe_name.setPlainText("")
        if self.ui.pb_add.text() == "add":
            stu_cnt = self.ui.lcdNumber.intValue()
            self.ui.lcdNumber.display(stu_cnt+ 1)


    def query(self,result,sendreg):
        self.sendreg={}
        output=str()
        if result["status"]== "Fail":
            self.ui.pb_add.setText("add")
            self.ui.lab_addstu.setText("    Add student")
            self.ui.lab_show.setText("Please input a subject name and score:")
            self.ui.txe_sj.setEnabled(True)
            self.ui.pb_add.setEnabled(True)
            self.ui.txe_score.setEnabled(True)
            self.ui.txe_name.setEnabled(False)
            self.ui.pb_query.setEnabled(False)
            self.sendreg["name"] = self.ui.txe_name.toPlainText()
            self.sendreg["scores"]={}
            return self.sendreg
        else:
            self.ui.pb_add.setText("modify")
            self.ui.lab_addstu.setText("    Modify student")
            for sj,sc in result["scores"].items():
                output=output + " " + sj
            self.ui.lab_show.setText(f"current subjects are {output}")
            self.ui.txe_sj.setEnabled(True)
            self.ui.pb_add.setEnabled(True)
            self.ui.txe_score.setEnabled(True)
            self.ui.txe_name.setEnabled(False)
            self.ui.pb_query.setEnabled(False)
            self.sendreg["name"] = self.ui.txe_name.toPlainText()
            self.sendreg["scores"]=result["scores"]
            return self.sendreg


    def show(self,result,sendreg):
        self.cnt=0
        self.ui.cb_del.clear()
        if result['status'] == 'OK':
            output = "\n==== student list ====\n\n"
            for name, data in result['parameters'].items():
                self.cnt+=1
                self.ui.cb_del.addItem(name)
                output += "name: " + data['name'] + "\n"
                for sub, sco in data['scores'].items():
                    output += "  subject: " + sub + ",  score: " + str(sco) + "\n"
                output += "\n"
            output += "======================\n"
        self.ui.lab_show.setText(f"Select the student to delete")
        self.ui.tx_show.setPlainText(output)
        self.ui.lcdNumber.display(self.cnt)
        