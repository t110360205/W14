from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QIntValidator,QDoubleValidator
from PyQt6.QtWidgets import  QStyledItemDelegate, QLineEdit

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=500))
        self.setText(content)


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=400, font_size=16,only_int=False):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        if only_int:
            self.setValidator(QIntValidator())
        self.setMinimumWidth(int(width/2))
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))

class NumericLineEditDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        validator = QDoubleValidator()
        editor.setValidator(QIntValidator(0, 999))  
        return editor
    
class TableComponent(QtWidgets.QTableWidget):
    def __init__(self,row=1,column=1,font_size=16,only_int=True):
        super().__init__()
        self.setRowCount(row)
        self.setColumnCount(column)
        self.setFont(QtGui.QFont("Arial", font_size))
        numeric_delegate = NumericLineEditDelegate()
        self.setItemDelegate(numeric_delegate)

class RadioComponent(QtWidgets.QRadioButton):
    def __init__(self,text="",font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))

class ComboboxComponent(QtWidgets.QComboBox):
    def __init__(self,font_size=16,item_lst=[]):
        super().__init__()
        for i in item_lst:
            self.addItem(str(i))
        self.setFont(QtGui.QFont("Arial", font_size))