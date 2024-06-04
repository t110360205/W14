import sys
import os
sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
sys.path.append(sql_path)
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from Studentsj import Studentsj
class Modify:
    def __init__(self,data={}):
        self.back={}
        self.data=data
        DBConnection.db_file_path = "sql/example.db"
        DBInitializer().execute()
    def indata(self):
        try:
            self.id=StudentInfoTable().select_a_student(self.data['parameters']['name'])
            Studentsj().delete_a_student(self.id[0])
            for subject,score in self.data['parameters']['scores_dict'].items():
                Studentsj().insert_a_student(self.id[0],subject,score)
            self.back['status'] = 'OK'
        except:
            self.back['status'] = 'Fail'
        print(self.back)
        return self.back
#The client sent data => {'command': 'modify', 'parameters': {'name': 'Test2', 'scores_dict': {'Python': 19.0, 'Eng': 100.0}}}
#The client received data => {'status': 'OK'}
  