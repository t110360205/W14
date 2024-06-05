from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.ModifyStuWidget import ModifyStuWidget
from WorkWidgets.WidgetComponents import LabelComponent
from WorkWidgets.WidgetComponents import ButtonComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QVBoxLayout()
        
        self.page_table = QtWidgets.QTabWidget()
        self.page_table.addTab(AddStuWidget(), "ADD")
        self.page_table.addTab(ModifyStuWidget(), "MODIFY")
        self.page_table.addTab(ShowStuWidget(), "SHOW")
        self.page_table.tabBarClicked.connect(self.page_table_change)
        layout.addWidget(self.page_table, stretch=1)
        self.setLayout(layout)

        with open('Client/WorkWidgets/style.css', 'r') as f:
            text = f.read()
            self.setStyleSheet(text)

        self.page_table.currentWidget().load()



    def page_table_change(self, index):
        self.page_table.widget(index).load()
        # print(self.page_table.currentWidget())

 