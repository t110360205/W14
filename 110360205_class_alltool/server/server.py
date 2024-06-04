from threading import Thread
from Add import Add
from Print import Print
from Query import Query
from Modify import Modify
from Del import Del
import socket
import json
BUFFER_SIZE = 1940
host = "127.0.0.1"
port = 20001
select={
    'add':Add,
    "show":Print,
    'query':Query,
    'delete':Del,
    'modify':Modify
        
}
class SocketServer(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # The following setting is to avoid the server crash. So, the binded address can be reused
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def serve(self):
        self.start()

    def run(self):
        while True:
            connection, address = self.server_socket.accept()
            print("{} connected".format(address))
            self.new_connection(connection=connection,
                                address=address)

    def new_connection(self, connection, address):
        Thread(target=self.receive_message_from_client,
            kwargs={
               "connection": connection,
                "address": address}, daemon=True).start()

    def receive_message_from_client(self, connection, address):
        keep_going = True
        while keep_going:
            try:
                while True:
                    message= connection.recv(BUFFER_SIZE).strip().decode()
                    try:
                        message = json.loads(message)
                        break
                    except:
                        pass
            except Exception as e:
                print("Exeption happened {}, {}".format(e, address))
                keep_going = False
            else:
                if not message:
                    keep_going = False
                if message['command'] == "close":
                    connection.send("closing".encode())
                    keep_going = False
                else:
                    if 'command' in message:
                        reply_msg = select[message['command']](message).indata()
                    print(message)
                    print('    server received:"command":' + message['command'] + ',"parameters":{} from'.format(message['parameters']) + str(address))
                    connection.send(json.dumps(reply_msg).encode())
        connection.close()
        print("{} close connection".format(address))

if __name__ == '__main__':
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()

    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server.server_socket.close()
    print("leaving ....... ")
