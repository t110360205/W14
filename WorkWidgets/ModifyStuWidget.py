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
    

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        self.client = SocketClient(host, port)
        student_dict = dict()
        self.student_dict = student_dict
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Modify Student")
        layout.addWidget(header_label, stretch=1)

        self.student_combo_box = QtWidgets.QComboBox()
        #self.student_combo_box.move(200, 100)
        self.student_combo_box.currentIndexChanged.connect(self.student_score)
        self.student_combo_box.currentIndexChanged.connect(self.student_subject)
        layout.addWidget(self.student_combo_box, stretch=1)

        self.score_label = LabelComponent(15, "Score: N/A")
        layout.addWidget(self.score_label, stretch=1)
       
        self.subject_combo_box = QtWidgets.QComboBox()
        self.subject_combo_box.move(200, 150)
        layout.addWidget(self.subject_combo_box, stretch=1)

        self.change_score_label = LineEditComponent("score", min_value=0, max_value=100)
        self.change_score_label.setValidator(QtGui.QIntValidator())
        self.change_score_label.mousePressEvent = self.clear_editor_content
        layout.addWidget(self.change_score_label)

        delete_button = ButtonComponent("Modify")
        delete_button.clicked.connect(self.modify_student)
        layout.addWidget(delete_button, stretch=1)
        self.student_combo_box.setStyleSheet("background-image: none;")
        self.score_label.setStyleSheet("background-image: none;")
        self.setLayout(layout)
        #self.apply_styles()

    def load(self):
        self.student_combo_box.clear()
        command = "load"
        self.client.send_command(command)
        self.response = self.client.wait_response()
        print(self.response)
        #data_parameters = response.get('parameters', {})
        keys = self.response.keys()
        for key in keys:
            self.student_combo_box.addItem(key)
        


    def student_score(self):
        name = self.student_combo_box.currentText()
        if name in self.response and "scores" in self.response[name]:
            scores = self.response[name]["scores"]
            self.score_label.setText(f"Score: {scores}")
        else:
            self.score_label.setText("Score: N/A")


    
    def student_subject(self):
        self.subject_combo_box.clear()
        name = self.student_combo_box.currentText()
        if name in self.response and "scores" in self.response[name]:
            scores = self.response[name]["scores"]
            keys = scores.keys()
            for key in keys:
                self.subject_combo_box.addItem(key)


    def modify_student(self):
        command = "modify"
        name = self.student_combo_box.currentText()
        subject = self.subject_combo_box.currentText()
        score = self.change_score_label.text()
        student_dict = {"name":name,"scores":{subject:score}}
        self.client.send_command(command,student_dict)
        self.client.wait_response()
        self.load()

    def clear_editor_content(self, event):
        self.change_score_label.clear()