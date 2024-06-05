from DBcontroller.StudentInfoTable import StudentInfoTable
from DBcontroller.SubjectInfoTable import SubjectInfoTable

class QueryStu():
    def __init__(self, student, data):
        self.student_dict = student
        self.data = data

    # def execute(self):
    #     status = 'OK'
    #     if  self.data["name"] in self.student_dict:
    #         reply_msg = {'status': status, 'scores':self.student_dict[self.data["name"]]['scores']}
    #     else :
    #         status = 'fail'
    #         reason = 'The name is not found.' 
    #         reply_msg = {'status': status, 'reason':reason}
    #     return reply_msg
    
    def execute(self):
        status = 'OK'

        index = StudentInfoTable().select_a_student(self.data["name"])

        if  len(index):
            score = SubjectInfoTable().select_a_student(index[0])
            print("score from sql: ", score)
            reply_msg = {'status': status, 'scores':score}
        else :
            status = 'fail'
            reason = 'The name is not found.' 
            reply_msg = {'status': status, 'reason':reason}
        return reply_msg
    