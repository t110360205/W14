from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent,RadioBtnComponent, ComboboxComponent
# from SocketClient.SocketClient import SocketClient
from SocketClient.SocketController import ExecuteSocket
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # self.client = SocketClient(host, port)
        self.cmd_stu_buf = dict()
        self.student_dict = dict()
        self.send_buffer = dict()

        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        self.add_student_btn = RadioBtnComponent("Add Student",connect=self.radio_btn_action, checked=True)
        self.add_subject_btn = RadioBtnComponent("Add Subject", connect=self.radio_btn_action)

        header_label = LabelComponent(20, "Add Student")
        name_label = LabelComponent(16, "Name: ")
        self.name_editor = LineEditComponent("Name")
        self.name_editor.mousePressEvent = self.clear_name_editor_content
        self.query_btn = ButtonComponent("Query", connect=self.query_action, disable=True)

        self.name_box = ComboboxComponent(connect=self.name_box_change, hide=True)

        sub_label = LabelComponent(16, "Subject: ")
        self.sub_editor = LineEditComponent("Subject", disable=True)
        self.sub_editor.mousePressEvent = self.clear_subject_editor_content

        score_label = LabelComponent(16, "Score: ")
        self.score_editor = LineEditComponent("")
        self.score_editor.setValidator(QtGui.QIntValidator())
        
        self.add_buffer_btn = ButtonComponent("Add", connect=self.add_buffer_action, disable=True)

        self.hint_label = LabelComponent(16, "Add Student Subject\nPress send to add\nPress clear to clear all content")
        self.hint_label.setStyleSheet("color:red;")

        self.send_btn = ButtonComponent("Send", connect=self.send_action, disable=True)
        self.clear_btn = ButtonComponent("Clear", connect=self.clear_action)

        
        layout.addWidget(self.add_student_btn, 1, 0, 1, 1)
        layout.addWidget(self.add_subject_btn, 2, 0, 1, 1)

        layout.addWidget(header_label, 0, 0, 1, 3)

        layout.addWidget(name_label, 1, 1, 1, 1)
        layout.addWidget(self.name_editor, 1, 2, 1, 1)
        layout.addWidget(self.name_box, 1, 2, 1, 1)
        layout.addWidget(self.query_btn, 1, 3, 1, 1)

        layout.addWidget(sub_label, 2, 1, 1, 1)
        layout.addWidget(self.sub_editor, 2, 2, 1, 1)

        layout.addWidget(score_label, 3, 1, 1, 1)
        layout.addWidget(self.score_editor, 3, 2, 1, 1)
        layout.addWidget(self.add_buffer_btn, 3, 3, 1, 1)

        layout.addWidget(self.hint_label, 0, 2, 1, 2)
        
        layout.addWidget(self.clear_btn, 5, 0, 1, 1)
        layout.addWidget(self.send_btn, 5, 4, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 4)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 1)

        layout.setRowStretch(0, 3)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 2)
        layout.setRowStretch(5, 2)

        self.setLayout(layout)
        
    def load(self):
        self.show_cmd = ExecuteSocket('show', {})
        self.show_cmd.result_sig.connect(self.show_process)
        self.show_cmd.start()

        self.name_box.clear()
        print("AddStu_init")

    def show_process(self, result):
        result = json.loads(result)
        self.student_dict = result["parameters"]
        for name, values in result["parameters"].items():
            self.name_box.addItem(name)

    def clear_name_editor_content(self, event):
        self.name_editor.clear()
        self.query_btn.setDisabled(False)
    
    def clear_subject_editor_content(self, event):
        self.sub_editor.clear()
        self.add_buffer_btn.setDisabled(False)

    def clear_all(self):
        self.query_btn.setDisabled(True)
        self.add_buffer_btn.setDisabled(True)

        self.sub_editor.setDisabled(True)
        self.sub_editor.setText("Subject")
        self.score_editor.setText("")

        self.name_editor.setText("Name")
        self.name_editor.setDisabled(False)

        self.name_box.setCurrentIndex(-1)

    def query_action(self):
        if not self.name_editor.text():
            return
        data =  {'name':self.name_editor.text()}
        self.send_buffer = data
        self.query_command = ExecuteSocket('query', data) 
        self.query_command.result_sig.connect(self.query_process)
        self.query_command.start()
        
    def query_process(self, result):    
        result = json.loads(result)

        name = self.send_buffer["name"]

        if result["status"] == "OK" :
            text = "The student's {} has existed.".format(name)
            self.hint_label.setText(text)
            return 
        else :
            text = "Please enter subjects for student '{}'".format(name)
            self.cmd_stu_buf["name"] = name
            self.cmd_stu_buf["scores"] = dict()

            print(text)
            self.query_btn.setDisabled(True)
            self.name_editor.setDisabled(True)
            self.sub_editor.setDisabled(False)
        self.hint_label.setText(text)

    def add_buffer_action(self):
        subject = self.sub_editor.text()      
        score = self.score_editor.text()
        if not(score and subject):
            return          
        if self.add_student_btn.isChecked():
            put_content = "scores"
        else :
            put_content = "scores_dict"
        self.cmd_stu_buf[put_content][subject] = self.score_editor.text()
        
        # self.hint_label.setText(text)
        self.send_btn.setDisabled(False)

    def send_action(self):
        if self.add_student_btn.isChecked():
            command = 'add' 
            
        else:
            command = 'modify'

        print(command, self.cmd_stu_buf)
        self.send_command = ExecuteSocket(command, self.cmd_stu_buf)
        self.send_command.result_sig.connect(self.send_process)
        self.send_command.start()

    def send_process(self, result):    
        result = json.loads(result)

        if result["status"] != 'OK':
            text = "The information {} is fail. The reason is {}".format(json.dumps(self.cmd_stu_buf), result["reason"])
        else :
            text = "The information {} is sent.".format(json.dumps(self.cmd_stu_buf))
            self.cmd_stu_buf = dict()
            self.clear_all()

        self.hint_label.setText(text)

    def clear_action(self):
        self.clear_all()

    def name_box_change(self, name):
        self.cmd_stu_buf["name"] = name
        self.cmd_stu_buf["scores_dict"] = dict()
        self.sub_editor.setEnabled(True)

    def radio_btn_action(self):
        if self.add_student_btn.isChecked(): 
            self.name_box.hide()
            self.name_editor.show()
            self.query_btn.show()
        else: 
            self.name_box.setCurrentIndex(-1)
            self.name_editor.hide()
            self.name_box.show()
            self.query_btn.hide()
            
