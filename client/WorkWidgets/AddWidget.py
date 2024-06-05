from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent,RadioComponent,ComboboxComponent

from SocketClient import SocketClient
from PyQt6.QtCore import pyqtSignal
import json

class AddWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_widget")
        self.setWindowTitle("Add")
        function_widget=FunctionWidget()
        menu_widget=MenuWidget(function_widget.update_widget)
        blank_widget = QWidget()
        blank_widget.setStyleSheet("background-image: url(background3.jpg);")

        menu_widget.setStyleSheet("background-image: none;background-color:rgba(0, 0, 0, 0);color:black;")
        function_widget.setStyleSheet("background-image:none;background-color:rgba(0, 0, 0, 0);color:black;")

        layout=QtWidgets.QGridLayout()
        layout.addWidget(blank_widget,0,0,3,2)
        layout.addWidget(menu_widget, 0, 0, 1, 1)
        layout.addWidget(function_widget, 1, 0, 2, 2)
        self.setLayout(layout)

class MenuWidget(QtWidgets.QWidget):
    def __init__(self,update_widget_callback):
        super().__init__()
        #add_stu_widget=AddStuWidget()
        self.setObjectName("menu_widget")
        self.update_widget_callback=update_widget_callback
        radio_layout=QtWidgets.QHBoxLayout()
        add_student_radio=RadioComponent("Add Student")
        add_subject_radio=RadioComponent("Add Subject")
        add_student_radio.toggled.connect(lambda: self.update_widget_callback("add_student"))
        add_subject_radio.clicked.connect(lambda: self.update_widget_callback("add_subject"))
        
        add_student_radio.setChecked(True)


        radio_layout.addWidget(add_student_radio)
        radio_layout.addWidget(add_subject_radio)
        self.setLayout(radio_layout)
        

class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.widget_dict = {
            "add_student": self.addWidget(AddStuWidget()),
            "add_subject": self.addWidget(AddSubject())
        }
        self.update_widget("add_student")
    
    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()
class AddSubject(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.add_dict={}
        self.setObjectName("add_subject")


        self.layout = QtWidgets.QGridLayout()

        self.message=LabelComponent(16,"")
        self.message.setStyleSheet("background-image:none;background-color:rgba(255,255, 255, 200);color:red;")
        self.message.setWordWrap(True)
        self.layout.addWidget(self.message,0,3,4,2)

        header_label = LabelComponent(20, "Add Subject")

        name_label = LabelComponent(16, "Name: ")
        self.combobox_name_label = ComboboxComponent()
        self.combobox_name_label.currentIndexChanged.connect(self.combobox_name_label_index_changed_action)


        subject_label=LabelComponent(16,"Subject: ")
        self.editor_subject_label=LineEditComponent("Subject")
        self.editor_subject_label.mousePressEvent = self.editor_subject_action

        score_label=LabelComponent(16,"Score: ")
        self.editor_score_label=LineEditComponent("",only_int=True)
        self.editor_score_label.setMaxLength(3)
        self.editor_score_label.mousePressEvent = self.editor_score_action
        
        self.add_button=ButtonComponent("Add")
        self.add_button.clicked.connect(self.add_button_action)
        self.add_button.setEnabled(False)
        
        self.send_button = ButtonComponent("Send")
        self.send_button.clicked.connect(self.send_button_action)
        self.send_button.setEnabled(False)

        self.layout.addWidget(header_label, 0, 0, 1, 2)
        self.layout.addWidget(name_label, 1, 0, 1, 1)
        self.layout.addWidget(self.combobox_name_label, 1, 1, 1, 1)
        self.layout.addWidget(subject_label,2,0,1,1)
        self.layout.addWidget(self.editor_subject_label,2,1,1,1)
        self.layout.addWidget(score_label,3,0,1,1)
        self.layout.addWidget(self.editor_score_label,3,1,1,1)
        self.layout.addWidget(self.add_button,3,2,1,1)
        self.layout.addWidget(self.send_button, 4, 4, 2, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setColumnStretch(3, 9)
        self.layout.setColumnStretch(4, 9)

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(3, 5)
        self.layout.setRowStretch(4, 5)

        self.setLayout(self.layout)
    
    def editor_subject_action(self,event):
        self.editor_subject_label.clear()
    def editor_score_action(self, event):
        self.add_button.setEnabled(True)
    
    def combobox_name_label_index_changed_action(self):
        if self.combobox_name_label.currentText()!="":
            self.query=ExecuteSend("query",{'name':self.combobox_name_label.currentText()})
            self.query.start()
            self.query.return_sig.connect(self.one_student_info_change)
            self.query.quit()
    def one_student_info_change(self,response):
        response_load =json.loads(response)
        print(f"response:{response_load}")
        self.one_student_info=response_load['scores']
    def add_button_action(self):
        if self.editor_subject_label.text()!=""and self.editor_score_label.text()!="":
            self.combobox_name_label.setEnabled(False)
            if self.editor_subject_label.text() not in self.one_student_info:
                self.one_student_info[self.editor_subject_label.text()]=self.editor_score_label.text()
                self.message.setText(f"Add [{self.combobox_name_label.currentText()},{self.editor_subject_label.text()},{self.editor_score_label.text()}] success!")
                self.send_button.setEnabled(True)
                self.editor_subject_label.clear()
                self.editor_score_label.clear()
            else:
                self.message.setText("This subject already exists!")
        else:
            self.message.setText("The subject or score is empty.")
  

    #def add_dict_change(self,response):
    #    print(self.add_dict)
    #    response_load =json.loads(response)
    #    self.add_dict=response_load['scores']
    #    name=self.combobox_name_label.currentText()
    #    subject=self.editor_subject_label.text()
    #    if subject not in self.add_dict:
    #        self.send_button.setEnabled(True)
    #        try:
    #            score=self.editor_score_label.text()
    #            score=float(score)
    #                
    #            self.add_dict[subject]=score
    #
    #            self.message.setText(f"Add [{name},{subject},{score}] success")   #詢問database有沒有此資料
    #            self.editor_score_label.clear()
    #            self.editor_subject_label.clear()
    #            
    #            self.add_button.setEnabled(False)
    #        except Exception as e:
    #            print(e)
    #    else:
    #        self.message.setText("This subject already exist.")
    #        self.add_dict={}
    #    print(self.add_dict)
    def send_button_action(self):
        self.load()
        send_message={'name':self.combobox_name_label.currentText(),'scores_dict':self.one_student_info}
        self.send=ExecuteSend("modify",send_message)
        self.send.start()
        self.send.return_sig.connect(self.send_button_judge)
        self.send.quit()
    def send_button_judge(self,response):
        response_load =json.loads(response)
        if response_load['status'].lower()=='ok':
            self.message.setText("Modify success!")
    def load(self):
        self.all_name_query=ExecuteSend("allname","")
        self.all_name_query.start()
        self.all_name_query.return_sig.connect(self.change_combobox)
        self.all_name_query.quit()
        self.message.setText("")
        self.editor_subject_label.clear()
        self.editor_score_label.clear()
        self.send_button.setEnabled(False)
    def change_combobox(self,response):
        self.combobox_name_label.clear()
        response_load =json.loads(response)
        print(f"response_load:{response_load}")
        for i in response_load['parameters']:
            self.combobox_name_label.addItem(i)
class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.add_dict={"name":"","scores":{}}
        self.setObjectName("add_stu_widget")

        self.layout = QtWidgets.QGridLayout()

        self.message=LabelComponent(16,"")
        self.message.setStyleSheet("background-image:none;background-color:rgba(255,255, 255, 200);color:red;")
        self.message.setWordWrap(True)
        self.layout.addWidget(self.message,0,3,4,2)

        header_label = LabelComponent(20, "Add Student")
        name_label = LabelComponent(16, "Name: ")
        self.editor_name_label = LineEditComponent("Name")
        self.editor_name_label.mousePressEvent = self.editor_name_action
        self.query_button=ButtonComponent("Query")
        self.query_button.clicked.connect(self.query_button_action)
        self.query_button.setEnabled(False)

        subject_label=LabelComponent(16,"Subject: ")
        self.editor_subject_label=LineEditComponent("Subject")
        self.editor_subject_label.setEnabled(False)
        self.editor_subject_label.mousePressEvent = self.editor_subject_action

        score_label=LabelComponent(16,"Score: ")
        self.editor_score_label=LineEditComponent("",only_int=True)
        self.editor_score_label.setMaxLength(3)
        self.editor_score_label.setDisabled(True)
        self.editor_score_label.setEnabled(False)
        self.editor_score_label.mousePressEvent = self.editor_score_action
        
        self.add_button=ButtonComponent("Add")
        self.add_button.clicked.connect(self.add_button_action)
        self.add_button.setEnabled(False)
        
        self.send_button = ButtonComponent("Send")
        self.send_button.clicked.connect(self.send_button_action)
        self.send_button.setEnabled(False)

        self.layout.addWidget(header_label, 0, 0, 1, 2)
        self.layout.addWidget(name_label, 1, 0, 1, 1)
        self.layout.addWidget(self.editor_name_label, 1, 1, 1, 1)
        self.layout.addWidget(self.query_button,1,2,1,1)
        self.layout.addWidget(subject_label,2,0,1,1)
        self.layout.addWidget(self.editor_subject_label,2,1,1,1)
        self.layout.addWidget(score_label,3,0,1,1)
        self.layout.addWidget(self.editor_score_label,3,1,1,1)
        self.layout.addWidget(self.add_button,3,2,1,1)
        self.layout.addWidget(self.send_button, 4, 4, 2, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setColumnStretch(3, 9)
        self.layout.setColumnStretch(4, 9)

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(3, 5)
        self.layout.setRowStretch(4, 5)

        self.setLayout(self.layout)

    def editor_name_action(self, event):
        self.editor_name_label.clear()
        self.query_button.setEnabled(True)
        self.add_button.setEnabled(False)
    def editor_subject_action(self,event):
        self.editor_subject_label.clear()
    def editor_score_action(self, event):
        self.add_button.setEnabled(True)
    #button
    def query_button_action(self,layout):

        
        if self.editor_name_label.text()!="":
            self.query=ExecuteSend("query",{'name':self.editor_name_label.text()})
            self.query.start()
            self.query.return_sig.connect(self.query_judge)
        else:
            self.message.setText("The name is empty.")
    def query_judge(self,response):
        response_load =json.loads(response)
        self.message.setText(str(response_load))
        if response_load['status']=='Fail':
            self.add_button.setEnabled(True)
            self.editor_score_label.setEnabled(True)
            self.editor_subject_label.setEnabled(True)
            self.editor_name_label.setEnabled(False)
            self.query_button.setEnabled(False)


        
    def add_button_action(self):
        if self.editor_subject_label.text()!=""and self.editor_score_label.text()!="":
            self.query_button.setEnabled(False)
            self.send_button.setEnabled(True)


            name=self.editor_name_label.text()
            subject=self.editor_subject_label.text()
            try:
                score=self.editor_score_label.text()
                score=float(score)
                
                self.add_dict['name']=name
                self.add_dict['scores'][subject]=score 

                self.message.setText(f"Add [{name},{subject},{score}] success")   #詢問database有沒有此資料
                self.editor_score_label.clear()
                self.editor_subject_label.clear()

            except Exception as e:
                print(e)

            
        else:
            self.message.setText("The subject or score is empty.")

    def send_button_action(self):
        self.editor_name_label.clear()
        self.editor_subject_label.clear()
        self.editor_score_label.clear()
        self.editor_name_label.setEnabled(True)
        self.editor_subject_label.setEnabled(False)
        self.editor_score_label.setEnabled(False)
        self.query_button.setEnabled(True)
        self.add_button.setEnabled(False)
        self.send_button.setEnabled(False)

        self.query=ExecuteSend("add",self.add_dict)
        self.query.start()
        self.query.return_sig.connect(self.send_button_judge)


    def send_button_judge(self,response):
        response_load =json.loads(response)
        self.message.setText(str(response_load))
        if response_load['status'].lower()=='ok':
            self.message.setText("This imformation \""+str(self.add_dict)+"\"  has been added successfully.")
            self.add_dict={"name":"","scores":{}}
    def load(self):
        self.editor_name_label.clear()
        self.editor_subject_label.setText("Subject")
        self.editor_score_label.clear()
        self.editor_name_label.setEnabled(True)
        self.editor_subject_label.setEnabled(False)
        self.editor_score_label.setEnabled(False)
        self.query_button.setEnabled(True)
        self.add_button.setEnabled(False)
        self.send_button.setEnabled(False)
        self.message.setText("")
        


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


        
        
