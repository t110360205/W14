from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent, ScrollComponent
from SocketClient.SocketController import ExecuteSocket
import time
import json

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")

        layout = QtWidgets.QVBoxLayout()
        # layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "======== Student List ========")
        header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.content_label = LabelComponent(18, "")
        content_scroll =  ScrollComponent(self.content_label)

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(content_scroll, stretch=9)

        self.setLayout(layout)
    
    def load(self):
        self.show_cmd = ExecuteSocket('show', {})
        self.show_cmd.result_sig.connect(self.show_process)
        self.show_cmd.start()
        print("ShowStu_init")

    def show_process(self, result):
        result = json.loads(result)
        print(result["parameters"])
        text = str()
        for name, values in result["parameters"].items():
            text += "Name: {}\n".format(name)
            for key, value in values['scores'].items():
                text += "  subject: {}, score: {:.1f}\n".format(key, value)
            text += '\n'
        self.content_label.setText(text)
