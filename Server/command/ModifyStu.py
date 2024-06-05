from DBcontroller.StudentInfoTable import StudentInfoTable
from DBcontroller.SubjectInfoTable import SubjectInfoTable

class ModifyStu():
    def __init__(self, student, data):
        self.student_dict = student
        self.data = data

    # def execute(self):
    #     self.student_dict[self.data['name']]['scores'] = self.data['scores_dict']
    #     return {'status':'OK'}

    def execute(self):
        try:
            index = StudentInfoTable().select_a_student(self.data["name"])
            scores = SubjectInfoTable().select_a_student(index[0])
        except Exception as e:
            return {'status':"Fail", "reason":e}
        
        for key, value in self.data['scores_dict'].items():
            if key in scores :
                if self.data['scores_dict'][key] != scores[key]:
                    SubjectInfoTable().update_a_student(self.data['scores_dict'][key], index[0], key)
            else :
                SubjectInfoTable().insert_a_student(index[0], key, value)
        return {'status':'OK'}
         



































