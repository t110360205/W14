import sys
import os
sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
sys.path.append(sql_path)
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from Studentsj import Studentsj
class Query:
    def __init__(self,data={}):
        self.back={}
        self.data=data
        DBConnection.db_file_path = "sql/example.db"
        DBInitializer().execute()
    def indata(self):
        try:
            print("a")
            self.id=StudentInfoTable().select_a_student(self.data['parameters']['name'])
            subject=Studentsj().select_a_student(self.id[0])
            self.back['status'] = 'OK'
            self.back['scores'] ={}
            for sj,sc in subject:
                    self.back['scores'].update({sj:sc})
            
        except:
             self.back['status'] = 'Fail'
             self.back['reason'] = 'The name is not found.'


        print(self.back)
        return self.back
    #The client sent data => {'command': 'query', 'parameters': {'name': 'Test3'}}
    #The client received data => {'status': 'Fail', 'reason': 'The name is not found.'}
  