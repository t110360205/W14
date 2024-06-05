from DBcontroller.StudentInfoTable import StudentInfoTable
from DBcontroller.SubjectInfoTable import SubjectInfoTable

class PrintAll():
    def __init__(self, student, data):
        self.student_dict = student
        self.data = data

    def execute(self):
        students = StudentInfoTable().select_all_student()
        student_dict = dict()
        print(students)
        for id, student in students.items():
            print(id, student)
            student_dict[student] = dict()
            student_dict[student]["name"] = student
            student_dict[student]["scores"] = SubjectInfoTable().select_a_student(id)

        status = 'OK'
        return {'status': status, 'parameters':student_dict}
    # def execute(self):
    #     status = 'OK'
    #     return {'status': status, 'parameters':self.student_dict}
