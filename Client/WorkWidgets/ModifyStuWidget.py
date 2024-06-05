from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent, ScrollComponent, ListComponent
from SocketClient.SocketController import ExecuteSocket
import json
from functools import partial

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.student_dict = dict()
        self.send_buffer = dict()

        self.setObjectName("modify_stu_widget")
  
        layout = QtWidgets.QHBoxLayout()
        block_left = QtWidgets.QVBoxLayout()
        block_right = QtWidgets.QVBoxLayout()
        
        self.name_list = ListComponent(self.name_change)
        self.score_list = ListComponent(self.score_change)

        name_list_scroll = ScrollComponent(self.name_list)
        score_list_scroll = ScrollComponent(self.score_list)

        self.del_btn = ButtonComponent("Delete", connect=self.del_btn_action)
        self.mod_btn = ButtonComponent("Modify", connect=self.mod_btn_action)

        block_left.addWidget(name_list_scroll, stretch=9)
        block_left.addWidget(self.del_btn, stretch=1)

        block_right.addWidget(score_list_scroll, stretch=9)
        block_right.addWidget(self.mod_btn, stretch=1)

        layout.addLayout(block_left, stretch=5)
        layout.addLayout(block_right, stretch=5)
        self.setLayout(layout)

    def load(self):
        self.show_cmd = ExecuteSocket('show', {})
        self.show_cmd.result_sig.connect(self.show_process)
        self.show_cmd.start()
        print("Modify_Stu_init")

    def show_process(self, result):
        result = json.loads(result)
        self.student_dict = result["parameters"]

        self.name_list.clear()
        self.score_list.clear()

        for name, values in result["parameters"].items():
            self.name_list.addItem(name) 

    def del_btn_action(self):
        result = self.message_confirm()
        if result == False:
            return 
        self.del_command = ExecuteSocket('delete', {"name":self.name_list.currentItem().text()})
        self.del_command.result_sig.connect(self.del_process)
        self.del_command.start()

    def del_process(self, result):
        result = json.loads(result)
        if result["status"] == 'OK':
            self.name_list.takeItem(self.name_list.currentRow())

    def mod_btn_action(self):   
        if self.score_list.currentRow() == -1:
            return
        self.score_change()

    def set_score_list(self, name):
        self.score_list.clear()
        for key, value in self.student_dict[name]['scores'].items():
            text = "  subject: {}, score: {:.1f}".format(key, value)
            self.score_list.addItem(text)

    def name_change(self):
        text = str()
        name = self.name_list.currentItem().text()
        self.set_score_list(name)

    def score_change(self):
        _subject = self.score_list.currentItem().text().split(",")
        sbuject = _subject[0].split(":")[-1].strip()
        score = _subject[1].split(":")[-1].strip()
        score = self.Message_getint("Modify Student Score", "Enter the Score")
        if score == -1:
            return
        self.send_buffer = {"name":self.name_list.currentItem().text(), "scores_dict":{sbuject:score}}
        self.modify_cmd = ExecuteSocket('modify', self.send_buffer)
        self.modify_cmd.result_sig.connect(self.modify_process)
        self.modify_cmd.start()

    def modify_process(self, result):
        result = json.loads(result)
        if result["status"] == 'OK':
            name = self.send_buffer["name"]
            _subject = self.send_buffer["scores_dict"]
            subject = list(_subject.keys())[0]
            score = list(_subject.values())[0]
            self.student_dict[name]["scores"][subject] = score
            self.set_score_list(name)
            

    def message_confirm(self):
        reply = QtWidgets.QMessageBox.question(self, 'confirm', 'Are you sure to delete?')
        if str(reply) == 'StandardButton.Yes':
            reply = True
        else:
            reply = False
        return 
    
    def Message_getint(self, title='Enter the integer', content="Value"):
        number, okPressed = QtWidgets.QInputDialog.getInt(self, title, content, 0, 0, 100, 1)
        if okPressed:
            return number
        return -1
    
    def get_item_index(self, item, target):
        if target == None:
            return -1
        for i in range(item.count()):
            if item.itemText(i) == target:
                return i
        return -1 