from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
import socket 
from threading import Thread
import json
#from AddStu import AddStu
host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, student_dict):
        
        send_data = {'command': command , 'parameters': student_dict}
        self.client_socket.send(json.dumps(send_data).encode())

        return student_dict
    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = eval(data.decode())
        print("87")
        print(raw_data)
        print("87")
        #print(f"{raw_data}raw_date")
        #if select_result == "query":
        return raw_data

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        self.client = SocketClient(host, port)
        student_dict = dict()
        self.student_dict = student_dict
        super().__init__()
        self.setObjectName("add_stu_widget")
        #self.client_socket = client_socket  # 存储 client_socket
        #self.receiving_thread = Thread(target=self.receive_from_server)
        #self.receiving_thread.daemon = True
        #self.receiving_thread.start()

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        content_label = LabelComponent(16, "Name: ")
        subject_label = LabelComponent(16, "Subject: ")
        score_label = LabelComponent(16, "Score: ")
        self.editor_label = LineEditComponent("Name")
        self.editor_label.mousePressEvent = self.clear_editor_content
        self.editor_label.textChanged.connect(self.button_control)
        self.subject_label = LineEditComponent("Subject")
        self.score_label = LineEditComponent("Score")
        #self.subject_label.mousePressEvent = self.clear_editor_content
        #self.score_label.mousePressEvent = self.clear_editor_content
        self.subject_label.textChanged.connect(self.button_control)
        self.score_label.textChanged.connect(self.button_control)
        button = ButtonComponent("Send")
        #button.clicked.connect(self.confirm_action)
        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")  
        self.query_button.clicked.connect(self.print_qurey)
        self.add_button.clicked.connect(self.print_input_text)
        button.clicked.connect(self.send)
        self.text_label = QtWidgets.QLabel("")
        self.text_label.setWordWrap(True)

        layout.addWidget(header_label, 0, 0, 1, 1)
        layout.addWidget(self.text_label, 0, 3, 1, 1)
        layout.addWidget(content_label, 1, 0, 1, 1)
        layout.addWidget(self.editor_label, 1, 1, 1, 1)
        layout.addWidget(self.query_button,1, 2, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(self.subject_label, 2, 1, 1, 1)
        layout.addWidget(button, 4, 2, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        layout.addWidget(self.score_label, 3, 1, 1, 1)
        layout.addWidget(self.add_button,3, 2, 1, 1)

        #layout.setColumnStretch(0, 2)
        #layout.setColumnStretch(1, 2)
#
        #layout.setRowStretch(0, 1)
        #layout.setRowStretch(1, 4)
        #layout.setRowStretch(2, 2)
        #layout.setRowStretch(3, 5)

        self.setLayout(layout)

    def add(self,name, sub, score):
        print(name)
        self.student_dict["scores"][sub]= score
        print(self.student_dict)

    
    def button_control(self):
        if self.editor_label.text():
            self.query_button.setDisabled(False)  
        else:
            self.query_button.setDisabled(True)
        if self.subject_label.text() and self.score_label.text():
            self.add_button.setEnabled(True)
        else:
            self.add_button.setEnabled(False)

    def clear_editor_content(self, event):
        self.editor_label.clear()
        #elif event == self.score_label:
            #self.score_label.clear()
        #elif event == self.score_label:
            #self.subject_label.clear()

    def confirm_action(self):
        print(self.editor_label.text())
        
    def print_qurey(self):
        command = "query"
        name = self.editor_label.text()
        
        student_dict = {"name":name}
        self.client.send_command(command, student_dict)
        data = self.client.wait_response()
        name1 = data["name"]
        text = (f"Please enter subject for student '{name1}'")
        self.text_label.setText(text)
        self.student_dict = {'name':name , 'scores':{}}
    def print_input_text(self):
        name = self.editor_label.text()
        if len(name) == 0 :
            text =(f"Please enter the student's name")
        else:
            subject = self.subject_label.text()
            score = self.score_label.text()
            self.add(name, subject, score)
            text = (f"Student {name}'s subject {subject} with score {score} added")
            text = (f"{self.student_dict}added")
        self.text_label.setText(text)

    def send(self):
        command = "add"
        #name = self.editor_label.text()
        #subject = self.subject_label.text()
        #score = self.score_label.text()
        self.client.send_command(command, self.student_dict)
        text1 = (f"The imformation {self.student_dict} is send")
        self.text_label.setText(text1)
        self.client.wait_response()
    def load(self):
        pass
    

        
