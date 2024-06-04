import sys
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from Studentsj import Studentsj

DBConnection.db_file_path = "sql/studt.db"
DBInitializer().execute()
StudentInfoTable().reset()
Studentsj().reset()


#Studentsj().insert_a_student("e","600")
#StudentInfoTable().insert_a_student("Bill")
#StudentInfoTable().insert_a_student("John")
#StudentInfoTable().insert_a_student("12","Joe")
"""
student_id = StudentInfoTable().select_a_student("Joe")
#StudentInfoTable().delete_a_student("6")
print("student_id: {}".format(student_id))
StudentInfoTable().update_a_student("1", "Test1")
"""
