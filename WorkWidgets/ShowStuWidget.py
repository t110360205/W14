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
 
    def send_command(self, command, student_dict = None):
        
        send_data = {'command': command , 'parameters': student_dict}
        self.client_socket.send(json.dumps(send_data).encode())

        return student_dict
    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = eval(data.decode())
        return raw_data

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        self.client = SocketClient(host, port)
        student_dict = dict()
        self.student_dict = student_dict
        super().__init__()
        self.setObjectName("show_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Show Student")
        layout.addWidget(header_label, stretch=1)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        #self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setMinimumSize(400, 200)
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)  

        
        self.scroll_area.setWidget(self.scroll_content) 
        #self.scroll_area.setStyleSheet("background-image: none);")
        layout.addWidget(self.scroll_area)
        self.setLayout(layout)
        
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                background-image: none;
            }
        """)

        self.scroll_content.setStyleSheet("""
            QWidget {
                background-color: transparent;
                background-image: none;
            }
        """)

    def load(self):
        for i in reversed(range(self.scroll_layout.count())):
            widget_to_remove = self.scroll_layout.itemAt(i).widget()
            self.scroll_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)


        command = "show"
        self.client.send_command(command)
        response = self.client.wait_response()
        data_parameters = response.get('parameters', {})


        for name, data in data_parameters.items():
            student_label = LabelComponent(14, f"Name: {name}")
            self.scroll_layout.addWidget(student_label)
            for subject, score in data['scores'].items():
                subject_label = LabelComponent(14, f"   Subject: {subject}, Score: {score}")
                self.scroll_layout.addWidget(subject_label)

        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_content.setStyleSheet("background-image: none;")