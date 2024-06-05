from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

class Query:
    def __init__(self,parameters):
        self.name=parameters['name']
    def execute(self):
        student_id = StudentInfoTable().select_a_student(self.name)
        if bool(student_id):
            student_id=student_id[0]
            subject_and_scores=SubjectInfoTable().select_a_subject(student_id)
            subject_and_scores_dic={key:value for key,value in subject_and_scores}
            print(subject_and_scores_dic)
            reply={'status':"OK",'scores':subject_and_scores_dic}
        else:
            reply={'status': 'Fail', 'reason': 'The name is not found.'}
        
        return reply

            