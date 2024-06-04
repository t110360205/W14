import socket 
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command,student_dict):
        send_data =json.dumps( {'command': command,'parameters':student_dict})
        print("  The client sent data => " + send_data)
        self.client_socket.send(send_data.encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE).decode()
        print("  The client received data => " + data)
        raw_data = json.loads(data)
        if raw_data == "closing":
            return False,""
        
        return True , raw_data

if __name__ == '__main__':
    client = SocketClient(host, port)

    keep_going = True
    while keep_going:
        command = input(">>>")
        client.send_command(command)
        keep_going = client.wait_response() 
    