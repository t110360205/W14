from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
# from SocketClient.SocketClient import SocketClient
from SocketClient.SocketController import ExecuteSocket
import json


class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.student_dict = dict()

        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QGridLayout()

        self.add_btn = QtWidgets.QRadioButton()
        self.add_btn.setText("Add")
        self.add_btn.setChecked(True)
        self.change_btn = QtWidgets.QRadioButton()
        self.change_btn.setText("Change")

        self.add_btn.clicked.connect(self.radio_btn_action)
        self.change_btn.clicked.connect(self.radio_btn_action)

        name_label = LabelComponent(16, "Name: ")
        self.name_box = QtWidgets.QComboBox()
        self.name_box.currentTextChanged.connect(self.name_box_change)

        sub_label = LabelComponent(16, "Subject: ")
        self.sub_box = QtWidgets.QComboBox()
        self.sub_box.hide()

        self.sub_editor = LineEditComponent("")

        score_label = LabelComponent(16, "Score: ")
        self.score_editor = LineEditComponent("")
        self.score_editor.setValidator(QtGui.QIntValidator())

        self.modify_btn = ButtonComponent("Modify")
        self.modify_btn.clicked.connect(self.modify_action)

        self.clear_btn = ButtonComponent("Clear")
        self.clear_btn.clicked.connect(self.clear_action)


        self.hint_text = LabelComponent(16, "Modify Student Subject")

        layout.addWidget(self.add_btn, 1, 0, 1, 1)
        layout.addWidget(self.change_btn, 3, 0, 1, 1)

        layout.addWidget(name_label, 1, 1, 1, 1)
        layout.addWidget(self.name_box, 1, 2, 1, 1)

        layout.addWidget(sub_label, 2, 1, 1, 1)
        layout.addWidget(self.sub_box, 2, 2, 1, 1)
        layout.addWidget(self.sub_editor, 2, 2, 1, 1)

        layout.addWidget(score_label, 3, 1, 1, 1)
        layout.addWidget(self.score_editor, 3, 2, 1, 1)
        layout.addWidget(self.add_btn, 3, 3, 1, 1)

        layout.addWidget(self.clear_btn, 5, 0, 1, 1)
        layout.addWidget(self.modify_btn, 5, 3, 1, 1)
        
        layout.addWidget(self.hint_text, 0, 1, 1, 3)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 2)
        layout.setColumnStretch(3, 2)

        layout.setRowStretch(0, 2)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 2)
        layout.setRowStretch(5, 1)
        self.setLayout(layout)

    def load(self):
        self.show_cmd = ExecuteSocket('show', {})
        self.show_cmd.result_sig.connect(self.show_process)
        self.show_cmd.start()

        self.name_box.clear()
        self.sub_box.clear()
        print("Modify_Stu_init")

    def show_process(self, result):
        result = json.loads(result)
        self.student_dict = result["parameters"]
        for name, values in result["parameters"].items():
            self.name_box.addItem(name)

    def radio_btn_action(self):
        if self.add_btn.isChecked(): 
            self.sub_box.hide()
            self.sub_editor.show()
        else: 
            self.sub_editor.hide()
            self.sub_box.show()
    
    def name_box_change(self, name):
        self.sub_box.clear()
        if not name :
            return
        for key, value in self.student_dict[name]["scores"].items():
            self.sub_box.addItem(key)

    def modify_action(self):
        name = self.name_box.currentText()

        if self.add_btn.isChecked():
            subject = self.sub_editor.text()
        else :
            subject = self.sub_box.currentText()
        
        if not(name and subject and self.score_editor.text()):
            self.hint_text.setText("Please fill the all modify data")
            return

        self.student_dict[name]['scores'][subject] = self.score_editor.text()
        data =  {'name':name, 'scores_dict':self.student_dict[name]["scores"]}
        self.modify_command = ExecuteSocket('modify', data) 
        self.modify_command.result_sig.connect(self.modify_process)
        self.modify_command.start()
        
    def modify_process(self, result):    
        result = json.loads(result)

    def clear_action(self):
        pass

    
    # def mod_btn_action(self):
    #     modify = self.parentWidget().findChildren(ModifyStuWidget)[0]
    #     if self.name_list.currentRow() == -1:
    #         return
    #     # index = self.get_item_index(modify.name_box, self.name_list.item(self.name_list.currentRow()).text())
    #     modify.name_box.addItem(self.name_list.item(self.name_list.currentRow()).text())
    #     modify.name_box.setCurrentText(self.name_list.item(self.name_list.currentRow()).text())
    #     # print(self.parentWidget().ModifyStuWidget().name_box.currentText())
    #     self.parentWidget().setCurrentIndex(1)