from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

class DelStu:
    def __init__(self,parameters):
        self.name=parameters['name']
    def execute(self):
        stu_id=StudentInfoTable().select_a_student(self.name)[0]
        StudentInfoTable().delete_a_student(stu_id)
        SubjectInfoTable().delete_a_subject(stu_id)
        reply={"status":'OK'}
        return reply
