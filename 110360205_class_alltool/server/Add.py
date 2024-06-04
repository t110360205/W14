import sys
import os
sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
sys.path.append(sql_path)
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from Studentsj import Studentsj
class Add:
    def __init__(self,data={}):
        self.back={}
        self.data=data     
        DBConnection.db_file_path = "sql/example.db"
        DBInitializer().execute()
    def indata(self):
        self.back['status'] = 'OK'
        stu_id=StudentInfoTable().den_id()
        if stu_id[0]["max_id"] == None:
            stu_id[0]["max_id"]=0
        StudentInfoTable().insert_a_student(stu_id[0]["max_id"]+1,self.data['parameters']['name'])
        for subject,score in self.data['parameters']['scores'].items():
            Studentsj().insert_a_student(stu_id[0]["max_id"]+1,subject,score)
        return self.back