import sys
import os
sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
sys.path.append(sql_path)
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from Studentsj import Studentsj
class Del:
    def __init__(self,data={}):
        self.back={}
        self.data=data
        DBConnection.db_file_path = "sql/example.db"
        DBInitializer().execute()
    def indata(self):
        try:
            self.id=StudentInfoTable().select_a_student(self.data['parameters']['name'])
            StudentInfoTable().delete_a_student(self.id[0])
            Studentsj().delete_a_student(self.id[0])
            self.back['status'] = 'OK'
        except:
             self.back['status'] = 'Fail'
        print(self.back)
        return self.back
#The client sent data => {'command': 'delete', 'parameters': {'name': 'Test2'}}
#The client received data => {'status': 'OK'}
  