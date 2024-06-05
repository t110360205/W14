from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QIntValidator


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=500))
        self.setText(content)

        
class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", min_value=None, max_value=None,length=10, width=200, font_size=16):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))

        if min_value is not None and max_value is not None:
            # 创建整数验证器，并设置范围
            validator = QIntValidator()
            validator.setRange(min_value, max_value)
            self.setValidator(validator)


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))
