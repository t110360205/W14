from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.DelStuWidget import DelStuWidget
from WorkWidgets.ModifyStuWidget import ModifyStuWidget
from WorkWidgets.WidgetComponents import LabelComponent
from WorkWidgets.WidgetComponents import ButtonComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QGridLayout()
        header_label = LabelComponent(24, "Student Management System")
        function_widget = FunctionWidget()
        menu_widget = MenuWidget(function_widget.update_widget)

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(menu_widget, 1, 0, 1, 1)
        layout.addWidget(function_widget, 1, 1, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)

        self.setLayout(layout)


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        self.setObjectName("menu_widget")
        self.update_widget_callback = update_widget_callback

        layout = QtWidgets.QVBoxLayout()
        add_button = ButtonComponent("Add student")
        show_button = ButtonComponent("Show all")
        del_button = ButtonComponent("Del student")
        modify_button = ButtonComponent("Modify student")
        # https://medium.com/seaniap/python-lambda-函式-7e86a56f1996
        add_button.clicked.connect(lambda: self.update_widget_callback("add"))
        show_button.clicked.connect(lambda: self.update_widget_callback("show"))
        del_button.clicked.connect(lambda: self.update_widget_callback("del"))
        modify_button.clicked.connect(lambda: self.update_widget_callback("modify"))

        layout.addWidget(add_button, stretch=1)
        layout.addWidget(show_button, stretch=1)
        layout.addWidget(del_button, stretch=1)
        layout.addWidget(modify_button,stretch=1)

        self.setLayout(layout)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        delwid=DelStuWidget()
        delwid.setStyleSheet("background-image: url(OIP.jpg);")
        showwid = ShowStuWidget()
        showwid.setStyleSheet("background-image: url(easy3.jpg);")
        addwid=AddStuWidget()
        #addwid.setStyleSheet("background-image: url(photo1.jpg);")
        modifywid = ModifyStuWidget()
        modifywid.setStyleSheet("background-image: url(photo1.jpg);")
        
        self.widget_dict = {
            "add": self.addWidget(addwid),
            "show": self.addWidget(showwid),
            "del": self.addWidget(delwid),
            "modify": self.addWidget(modifywid)
        }
        self.update_widget("add")
    
    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()
