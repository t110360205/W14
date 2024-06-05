from SocketServer import SocketServer
from DB.DBConnection import DBConnection
from DB.DBInitializer import DBInitializer
def main():
    host = "127.0.0.1"
    port = 20001
    DBConnection.db_file_path = ".\\DB\\Database.db"
    DBInitializer().execute()
    server1 =SocketServer(host, port)
    server1.daemon = True
    server1.serve()
    # because we set daemon is true, so the main thread has to keep alive
    while True:
        command = input()
        if command == "finish":
            break
    
    server1.server_socket.close()
    print("leaving ....... ")


main()
