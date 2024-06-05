from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
def enter_server():
    student_dict = dict()
    student_dict1 = dict()
    student_dict2 = dict()
    #print(student_dict)
    student_info = StudentInfoTable().select_stu_id_column()
    #print(student_info)
    subject_info = StudentInfoTable().select_subject_column()
    #print(subject_info)
    for stu_id, name in student_info:
        student_dict1[stu_id] = {name:{'name': name, 'scores': {}}}
    for stu_id, subject, score in subject_info:
        student_dict1[stu_id][StudentInfoTable().select_stu_name_column(stu_id)[0]]['scores'][subject] = score
    #print('1')
    #print(student_dict1)
    #print('1')
    for key, value in student_dict1.items():
        for k, v in value.items():
            student_dict2 = {k: v}
            student_dict = {**student_dict, **student_dict2}
    print('1')
    print(student_dict)
    print('1')

    return student_dict