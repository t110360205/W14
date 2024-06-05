from threading import Thread
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
import enter_server
import socket
import json
import add_sever
import print_server
import modify_sever
import del_server
import query
host = "127.0.0.1"
port = 20001


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
        student_dict = dict()
        student_dict1 = dict()

        keep_going = True
        while keep_going:
            try:
                message = connection.recv(1024).strip().decode()
            except Exception as e:
                print("Exeption happened {}, {}".format(e, address))
                keep_going = False
            else:
                if not message:
                    keep_going = False
                else:
                    try:
                        message = json.loads(message)
                    except json.JSONDecodeError as e:
                        print("Error decoding JSON: {}, {}".format(e, address))
                        continue
                #print("1")
                #print(student_dict)
                print(message)
                
                if message['command'] == "exit":
                    connection.send("exit".encode())
                    keep_going = False
                else:
                    student_dict = enter_server.enter_server()
                    if message["command"] == "load":
                        connection.send(json.dumps(student_dict).encode()) 

                    if message["command"] == "query":
                       #if student_dict is  None:
                           #student_dict["parameters"] = {"name" : None}
                       student_dict1 = query.query(message , student_dict)
                       connection.send(json.dumps(student_dict1).encode()) 

                    if message['command'] == "add":
                        student_dict = add_sever.add_sever(message , student_dict)
                        student_dict['command'] = "add"
                        print(student_dict)                        
                        connection.send(json.dumps(student_dict).encode())
                        del student_dict['command']
                        name = message['parameters']['name']
                        subject = list(student_dict[name]['scores'].keys())
                        score =  list(student_dict[name]['scores'].values())
                        #print(name , subject, score)
                        StudentInfoTable().insert_a_student(name)
                        student_id = StudentInfoTable().select_a_student(name)[0]
                        for i in range( len(subject)):
                            StudentInfoTable().insert_a_subject(student_id, subject[i], score[i])

                    if message["command"] == "modify":
                        student_dict = modify_sever.modify_sever(message , student_dict)
                        student_dict['command'] = 'modify'
                        connection.send(json.dumps(student_dict).encode())
                        del student_dict['command']
                        #StudentInfoTable().update_a_student(self, student_dict, name)

                    if message["command"] == "del":
                        student_dict = del_server.del_server(message , student_dict)
                        student_dict['command'] = 'del'
                        connection.send(json.dumps(student_dict).encode())
                        del student_dict['command']  

                    if message['command'] == "show":
                        student_dict1 = print_server.print_server(message['command'],student_dict)
                        connection.send(json.dumps(student_dict1).encode())
                        print(f"show{student_dict1}success")
                        
        connection.close()
        print("{} close connection".format(address))


if __name__ == '__main__':
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()
    keep_going = True
    DBConnection.db_file_path = "example.db"
    DBInitializer().execute()
    # because we set daemon is true, so the main thread has to keep alive
    while keep_going :
        command = input()

        if command == "exit":
            break
    
    server.server_socket.close()
    print("leaving ....... ")