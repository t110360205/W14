from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent,RadioComponent,ComboboxComponent

from SocketClient import SocketClient
from PyQt6.QtCore import pyqtSignal
import json

class DelWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("del_widget")
        self.setWindowTitle("Del")

        layout=QtWidgets.QGridLayout()
        
        header_label = LabelComponent(20, "Delete Student")
        header_label.setStyleSheet("background-image:none;background-color:rgba(0, 0, 0, 0);color:black")

        name_label=LabelComponent(16,"Name:")
        name_label.setStyleSheet("background-image:none;background-color:rgba(0, 0, 0, 0);color:black")
        self.combobox_name_label = ComboboxComponent()
        
        send_button=ButtonComponent("Send")
        send_button.clicked.connect(self.send_button_action)
        send_button.setStyleSheet("background-image:none;background-color:rgba(0, 0, 0, 0);color:black")
        self.message=LabelComponent(16,"")
        self.message.setStyleSheet("color:red;")

        self.load()

        blank_widget = QWidget()
        blank_widget.setStyleSheet("background-image: url(background2.jpg);")

        layout.addWidget(blank_widget,0,0,2,4)
        layout.addWidget(header_label,0,0,1,3)
        layout.addWidget(name_label,1,0,1,1)
        layout.addWidget(self.combobox_name_label,1,1,1,2)
        layout.addWidget(send_button,1,3,1,1)
        layout.addWidget(self.message,0,4,2,1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 3)
        layout.setColumnStretch(3,2)
        layout.setColumnStretch(4,3)


        layout.setRowStretch(0, 1)
        layout.setRowStretch(1,9)
        layout.setRowStretch(2,9)


        self.setLayout(layout)
    def load(self):
        self.all_name_query=ExecuteSend("allname","")
        self.all_name_query.start()
        self.all_name_query.return_sig.connect(self.change_combobox)
        self.all_name_query.quit()
    def change_combobox(self,response):
        self.combobox_name_label.clear()
        response_load =json.loads(response)
        print(f"response_load:{response_load}")
        for i in response_load['parameters']:
            self.combobox_name_label.addItem(i)
    def send_button_action(self):
        if self.combobox_name_label.currentText()!="":
            message={"name":self.combobox_name_label.currentText()}
            self.del_sig=ExecuteSend("delete",message)
            self.del_sig.start()
            self.del_sig.return_sig.connect(self.del_judge)
            self.del_sig.quit()
        else:
            self.message.setText("All Deleted!!")
    def del_judge(self,response):
        response_load =json.loads(response)
        try:
            if response_load['status']=="OK":
                self.message.setText("Success")
            else:
                self.message.setText("Failed")
        except Exception as e:
            self.message.setText(e)
        self.load()
class ExecuteSend(QtCore.QThread):
    return_sig = pyqtSignal(str)

    def __init__(self,command,parameters):
        host = "127.0.0.1"
        port = 20001
        BUFFER_SIZE = 1940
        self.clinet=SocketClient(host,port)
        super().__init__()
        self.parameters=parameters
        self.command=command
    def run(self):
      
        self.clinet.send_command(self.command,self.parameters)
        response=self.clinet.wait_response()
        response=eval(response)
        self.return_sig.emit(json.dumps(response))
        self.clinet.send_command("exit","")
        response=self.clinet.wait_response()
        