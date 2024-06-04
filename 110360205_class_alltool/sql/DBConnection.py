import sys
import os
sys.path.append('../sql')
import sqlite3
from threading import Lock


class DBConnection:
    db_file_path = str()
    db_lock = Lock()

    def __init__(self):
        #project_root = os.path.dirname(os.path.dirname(__file__))
        # 設定資料庫文件的絕對路徑
        #self.db_file_path = os.path.join(project_root, 'sql', 'example.db')
        DBConnection.db_lock.acquire()
        self.connection = sqlite3.connect(self.db_file_path)
        # Sets the row_factory to the callable sqlite3.Row, which converts the plain tuple into a more useful object.
        self.connection.row_factory = sqlite3.Row

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        DBConnection.db_lock.release()
