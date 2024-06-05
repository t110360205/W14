from DB.StudentInfoTable import StudentInfoTable
from DB.SubjectInfoTable import SubjectInfoTable

class PrintAll:
    def __init__(self,parameters):
        pass
    def execute(self):
        student_name=StudentInfoTable().all_student_info_return()
        parameters={}
        for name in student_name:
            stu_id=StudentInfoTable().select_a_student(name)[0]
            subject_scores_tuple=SubjectInfoTable().select_a_subject(stu_id)
            subject_scores_dic={}
            for subject_scores in subject_scores_tuple:
                subject_scores_dic[subject_scores[0]]=subject_scores[1]
            name_scores={'name':name,'scores':subject_scores_dic}
            parameters[name]=name_scores
        reply={"status":'OK',"parameters":parameters}
        return reply