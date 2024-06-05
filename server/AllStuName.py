from DB.StudentInfoTable import StudentInfoTable


class AllStuName:
    def __init__(self,parameters):
        pass
    def execute(self):
        student_name=StudentInfoTable().all_student_info_return()
        parameters=student_name
        reply={"status":'OK',"parameters":parameters}
        return reply