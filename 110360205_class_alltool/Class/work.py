import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal
from Class.class_init import Ui_MainWindow 
from Class.ch_color import ch_color
from client.client import SocketClient 
import json
from Class.action_in import action_in
from Class.action_out import action_out
host = "127.0.0.1"
port = 20001
client = SocketClient(host, port)


class working:

    def __init__(self,ui):
        self.ui = ui
        self.sendreg=dict()

    def wait(self):
        ch_color(self.ui).color_init()
        self._translate = QtCore.QCoreApplication.translate
        self.pb_do_show()
        self.ui.pb_query.clicked.connect(lambda: self.pb_do_query())
        self.ui.pb_add.clicked.connect(lambda: self.pb_do_add_data())
        self.ui.pb_send.clicked.connect(lambda: self.pb_do_send())
        self.ui.pb_show.clicked.connect(lambda: self.pb_do_show())
        self.ui.pb_addstu.clicked.connect(lambda: self.pb_do_addmod())
        self.ui.pb_del1.clicked.connect(lambda: self.pb_do_ckdel())
        self.ui.pb_del2.clicked.connect(lambda: self.pb_do_ckdel2())

    def pb_do_show(self):
        self.command="show"
        self.ui.cb_del.setVisible(True)   
        self.ui.tx_show.setVisible(True)
        self.ui.pb_del1.setVisible(False)
        self.ui.pb_del2.setVisible(False) 
        self.ui.lab_addstu.setText("    Show student")
        self.ui.lab_name.setVisible(False)
        self.ui.lab_sj.setVisible(False)
        self.ui.lab_score.setVisible(False)
        self.ui.pb_query.setVisible(False)
        self.ui.pb_add.setVisible(False)
        self.ui.txe_sj.setVisible(False)
        self.ui.txe_score.setVisible(False)
        self.ui.txe_name.setVisible(False)
        self.ui.pb_send.setEnabled(True)
        self.send_command = ExecuteConfirmCommand("a",self.command)
        self.send_command.start()
        self.send_command.return_dict.connect(self.process_result)

    def pb_do_addmod(self):
        
        self.ui.tx_show.setVisible(False)
        self.ui.lab_addstu.setVisible(True)
        self.ui.lab_name.setVisible(True)
        self.ui.lab_sj.setVisible(True)
        self.ui.lab_score.setVisible(True)
        self.ui.pb_query.setVisible(True)
        self.ui.pb_add.setVisible(True)
        self.ui.pb_send.setVisible(True)
        self.ui.lab_show.setVisible(True)
        self.ui.txe_sj.setVisible(True)
        self.ui.txe_score.setVisible(True)
        self.ui.txe_name.setVisible(True)
        self.ui.pb_del1.setVisible(False)
        self.ui.pb_del2.setVisible(False) 
        self.ui.cb_del.setVisible(False)   
        self.ui.lab_show.setWordWrap(True)
        self.ui.txe_sj.setEnabled(False)
        self.ui.txe_score.setEnabled(False)
        self.ui.pb_add.setEnabled(False)
        self.ui.pb_send.setEnabled(False)

    def pb_do_query(self):
        self.command="query"
        self.send_command = ExecuteConfirmCommand(self.ui.txe_name.toPlainText(),self.command)
        self.send_command.start()
        self.send_command.return_dict.connect(self.process_result)

    def pb_do_add_data(self):
        self.command=self.ui.pb_add.text()
        
        match self.command:
            case "add":
                    self.ui.lab_show.setText(f"Student dsa's subject {str(self.ui.txe_sj.toPlainText())} with score {str(self.ui.txe_score.toPlainText())} added")
            case "modify":
                    if str(self.ui.txe_sj.toPlainText()) in self.sendreg:
                        self.ui.lab_show.setText(f"Student dsa's subject {str(self.ui.txe_sj.toPlainText())} with score {str(self.ui.txe_score.toPlainText())} mocify")
                    else:
                        self.ui.lab_show.setText(f"Student dsa's subject {str(self.ui.txe_sj.toPlainText())} with score {str(self.ui.txe_score.toPlainText())} added")
        self.sendreg["scores"].update({self.ui.txe_sj.toPlainText(): self.ui.txe_score.toPlainText()})
        print(self.sendreg)
        self.ui.txe_sj.setPlainText("")
        self.ui.txe_score.setPlainText("")  
        self.ui.pb_send.setEnabled(True)


    def pb_do_send(self):
        match self.command:
            case "add" | "modify":
                self.send_command = ExecuteConfirmCommand(self.sendreg,self.command)
                self.send_command.start()
                self.send_command.return_dict.connect(self.process_result)
            case "show" | "delete":
                self.ui.pb_send.setVisible(False)
                self.ui.pb_del1.setVisible(True)


    def pb_do_ckdel(self):
        self.ui.pb_del1.setVisible(False)
        self.ui.pb_del2.setVisible(True)       

    def pb_do_ckdel2(self):
        self.command="delete"
        self.ui.pb_del2.setVisible(False)
        self.ui.pb_send.setVisible(True)  
        self.send_command = ExecuteConfirmCommand(self.ui.cb_del.currentText(),self.command)
        self.send_command.start()
        self.send_command.return_dict.connect(self.process_result)
    
    def deltoshow(self,result,sendreg):
        self.pb_do_show()

    def process_result(self, result):
        act_in = {
        "add":action_in(self.ui).display_save,
        "modify":action_in(self.ui).display_save,
        "query":action_in(self.ui).query,
        "show":action_in(self.ui).show,
        "delete":self.deltoshow
        }
        result = json.loads(result)
        print(result)
        self.sendreg =act_in[self.command](result,self.sendreg)
        print(self.sendreg)

class ExecuteConfirmCommand(QtCore.QThread):
    return_dict = pyqtSignal(str)

    def __init__(self, counts,command):
        super().__init__()
        self.counts = counts
        self.com=command

    def run(self):
        act_out = {
        "add":action_out(4).add,
        "modify":action_out(4).mod,
        "query":action_out(4).combine_name,
        "show":action_out(4).show,
        "delete":action_out(4).combine_name
        }
        stu_dict=act_out[self.com](self.counts)
        print(stu_dict)
        client.send_command(self.com,stu_dict)
        keep_going,result_dict = client.wait_response()
        self.return_dict.emit(json.dumps(result_dict))

        
            


'''
if __name__ == "__main__":s
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())'''
