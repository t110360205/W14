import sys
import os
sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sql'))
sys.path.append(sql_path)
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from Studentsj import Studentsj
class Print:
    def __init__(self,data):
        self.back={}
        self.data=data
        DBConnection.db_file_path = "sql/example.db"
        DBInitializer().execute()
    def indata(self):
        self.back['status'] = 'OK'
        self.back['parameters'] ={}
        
        self.data=StudentInfoTable().select_print()
        for stu_id,name in self.data:
            self.back['parameters'].setdefault(name, {'name':name})
            subject=Studentsj().select_a_student(stu_id)
            self.back['parameters'][name]['scores']={}
            for sj,sc in subject:
                self.back['parameters'][name]['scores'].update({sj:sc})
        return self.back

        