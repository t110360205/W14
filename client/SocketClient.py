import socket 
import json
#from AddStu import AddStu
#from PrintAll import PrintAll

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command,parameters):
        send_data = {'command': command,'parameters':parameters}
        print(f"The client sent data => {send_data}")
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self): #更改command
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print(f"The client received data => {raw_data}")
        
        #if command=="show":
        #    PrintAll().print_all(eval(raw_data)["parameters"])
                
        return raw_data

