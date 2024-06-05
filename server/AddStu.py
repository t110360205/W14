from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

class AddStu:
    def __init__(self,parameters):
        self.name=parameters['name']
        self.subject_scores=parameters['scores']
    def execute(self):
        StudentInfoTable().insert_a_student(self.name)
        stu_id=StudentInfoTable().select_a_student(self.name)[0]
        for subject,scores in self.subject_scores.items():
            SubjectInfoTable().insert_a_subject(stu_id,subject,scores)
        reply={'status':"OK"}
        return reply