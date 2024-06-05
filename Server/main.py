from server import SocketServer 
from DBcontroller.DBConnection import DBConnection
from DBcontroller.DBInitializer import DBInitializer


host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940

def main():
    DBConnection.db_file_path = "./Server/example2.db"
    DBInitializer().execute()

    server = SocketServer(host, port)
    server.daemon = True
    server.serve()

    while True:
        command = input()
        if command == "finish":
            break
        print(command)

    server.server_socket.close()


if __name__ == '__main__':
    main()