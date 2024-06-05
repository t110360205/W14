from DBcontroller.StudentInfoTable import StudentInfoTable
from DBcontroller.SubjectInfoTable import SubjectInfoTable

class AddStu():
    def __init__(self, student, data):
        self.student_dict = student
        self.data = data

    # def execute(self):    #use dictionary way
    #     status = 'OK'

    #     name = self.data["name"]
    #     self.student_dict[name] = dict()
    #     self.student_dict[name]["name"] = name
    #     self.student_dict[name]["scores"] = dict()
        
    #     for key, value in self.data["scores"].items() :
    #         self.student_dict[name]["scores"][key] = value
            
    #     reply_msg = {'status': status}
    #     return reply_msg
    
    def execute(self):      #use database way
        status = 'OK'

        StudentInfoTable().insert_a_student(self.data["name"])
        index = StudentInfoTable().select_a_student(self.data["name"])
        
        for key, value in self.data["scores"].items() :
            SubjectInfoTable().insert_a_student(index[0], key, value)
            
        reply_msg = {'status': status}
        return reply_msg