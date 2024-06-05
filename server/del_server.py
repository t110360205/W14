from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
def del_server(message, student_dict):
    #print("1")
    name = message['parameters']["name"]
    #print(student_dict)
    student_id = StudentInfoTable().select_a_student(name)[0]
    print(student_id)
    Confirm  = message['parameters']["check"]
    if Confirm == "y":
        StudentInfoTable().delete_a_student(student_id)
        StudentInfoTable().delete_a_subject(student_id)
        del student_dict[name]
    return student_dict