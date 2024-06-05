from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent,TableComponent

import json
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QScrollArea, QTableWidgetItem
from SocketClient import SocketClient




class ShowStuWidget(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")
        
        self.student_info_table=TableComponent();
        #self.student_info_table.horizontalHeader().setStyleSheet("color:black; font-weight: bold;background-color: rgba(255, 255, 255, 0);")
        self.student_info_table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: rgba(255, 255, 255, 150); color: black; font-weight: bold; }")
        self.student_info_table.verticalHeader().setStyleSheet("QHeaderView::section { background-color: rgba(255, 255, 255, 150); color: black; font-weight: bold; }")
        self.student_info_table.setStyleSheet("background-color:rgba(255, 255, 255, 0);")
        self.student_info_table.cellChanged.connect(self.student_info_table_changed_action)
        self.load()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.student_info_table)
        self.setLayout(layout)
    def student_info_table_changed_action(self,row,column):
        name=self.student_info_table.verticalHeaderItem(row).text()
        sent_parameters={}
        sent_subject_to_score_dic={}
        for i in range(self.student_info_table.columnCount()):
            item=self.student_info_table.item(row,i)
            if item is not None:
                sent_subject_to_score_dic[self.student_info_table.horizontalHeaderItem(i).text()]=item.text()
        sent_parameters={'name':name,"scores_dict":sent_subject_to_score_dic}
        self.modify_table=ExecuteSend("modify",sent_parameters)
        self.modify_table.start()
        self.modify_table.return_sig.connect(self.modify_table_judge)
    def modify_table_judge(self):
        pass
    def load(self):
        self.show=ExecuteSend("show","")
        self.show.start()
        self.show.return_sig.connect(self.show_message)

    def show_message(self,response):
        self.student_info_table.cellChanged.disconnect(self.student_info_table_changed_action)
        response_load =json.loads(response)
        response_load =eval(str(response_load))
        #print(response_load)
        name_lst=[];subject_lst=[]
        name_to_subject_idx_to_score={}
        for name,name_scores in response_load['parameters'].items():
            name_lst.append(name)
            subject_idx_to_score_dic_temp={}
            for subject,score in name_scores["scores"].items():
                if subject not in subject_lst:
                    subject_lst.append(subject)
                subject_idx_to_score_dic_temp[subject_lst.index(subject)]=score
            name_to_subject_idx_to_score[name]=subject_idx_to_score_dic_temp
        #print(f"name_lst:{name_lst}")
        #print(f"name_to_subject_idx_to_score:{name_to_subject_idx_to_score}")
        #print(f"subject_lst:{subject_lst}")
        #print(f"scores_idx_lst:{scores_idx_lst}")
        #print(f"scores_lst:{scores_lst}")
        self.student_info_table.setRowCount(len(name_to_subject_idx_to_score))
        self.student_info_table.setColumnCount(len(subject_lst))
        for name,subject_idx_to_score_dic in name_to_subject_idx_to_score.items():
            name_idx=name_lst.index(name)
            self.student_info_table.setVerticalHeaderItem(name_idx,QTableWidgetItem(name))
            for subject_idx,score in subject_idx_to_score_dic.items():
                self.student_info_table.setItem(name_idx,subject_idx,QTableWidgetItem(str(score)))
        
        for subject in subject_lst:
            self.student_info_table.setHorizontalHeaderItem(subject_lst.index(subject),QTableWidgetItem(subject))
        
        self.student_info_table.cellChanged.connect(self.student_info_table_changed_action)

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