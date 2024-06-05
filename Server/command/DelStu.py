from DBcontroller.StudentInfoTable import StudentInfoTable
from DBcontroller.SubjectInfoTable import SubjectInfoTable

class DelStu():
    def __init__(self, student, data):
        self.student_dict = student
        self.data = data

    def execute(self):
        index = StudentInfoTable().select_a_student(self.data["name"])
        reply_msg = dict()
        try :
            SubjectInfoTable().delete_a_student(index[0])
            StudentInfoTable().delete_a_student(index[0])
            reply_msg = {'status': 'OK'}
        except Exception as e:
            reply_msg = {'status': 'Fail', 'reason':e}
            
        return reply_msg
