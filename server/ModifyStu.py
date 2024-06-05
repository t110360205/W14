from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

class ModifyStu:
    def __init__(self,parameters):
        self.name=parameters['name']
        self.scores=parameters['scores_dict']
    def execute(self):
        stu_id=StudentInfoTable().select_a_student(self.name)[0]
        SubjectInfoTable().delete_a_subject(stu_id)
        for subject,score in self.scores.items():
            SubjectInfoTable().insert_a_subject(stu_id,subject,score)
        reply={'status':"OK"}
        return reply