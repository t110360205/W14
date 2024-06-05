from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
#from PrintAll import PrintAll
import socket 
import json
host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, student_dict=None ):
        
        send_data = {'command': command , 'parameters': student_dict}
        self.client_socket.send(json.dumps(send_data).encode())

        return student_dict
    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = eval(data.decode())
        #raw_data = data.decode()
        return raw_data

class DelStuWidget(QtWidgets.QWidget):
    def __init__(self):
        self.client = SocketClient(host, port)
        student_dict = dict()
        self.student_dict = student_dict
        super().__init__()
        self.setObjectName("del_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Delete Student")
        layout.addWidget(header_label, stretch=1)

        self.student_combo_box = QtWidgets.QComboBox()
        self.student_combo_box.move(200, 100)
        layout.addWidget(self.student_combo_box, stretch=1)

        delete_button = ButtonComponent("Del")
        delete_button.clicked.connect(self.delete_student)
        layout.addWidget(delete_button, stretch=1)
        #.setStyleSheet("background-image: url(photo1.jpg);")
        self.setLayout(layout)

    def load(self):
        command = "load"
        self.client.send_command(command)
        response = self.client.wait_response()
        print(response)
        #data_parameters = response.get('parameters', {})
        keys = response.keys()
        self.student_combo_box.clear()
        for key in keys:
            self.student_combo_box.addItem(key)
        pass
    def delete_student(self):
        command = "del"
        name = self.student_combo_box.currentText()
        student_dict = {"name":name,"check":"y"}
        self.client.send_command(command,student_dict)
        self.client.wait_response()
        self.load()
    
    