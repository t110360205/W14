from PyQt6 import QtCore
from SocketClient.SocketClient import SocketClient
import json

host = "127.0.0.1"
port = 20001

class SocketController:
    client = SocketClient(host, port)#None
    
    def command_sender(self, command, data):
        self.client.send_command(command, data)
        return self.client.wait_response()


class ExecuteSocket(QtCore.QThread):
    result_sig = QtCore.pyqtSignal(str)

    def __init__(self, command, data):
        super().__init__()
        self.command = command
        self.data = data
        
    def run(self):
        result = SocketController().command_sender(self.command, self.data)
        self.result_sig.emit(json.dumps(result))