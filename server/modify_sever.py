from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
def modify_sever(message, student_dict):
    student_dict1 = dict()
    subject_dict = dict()
    #print("777")
    #print(message)
    #print(student_dict)
    #print("777")
    data = message['parameters']
    name = data['name']
    student_id = StudentInfoTable().select_a_student(name)[0]
    subject_client =list(data['scores'].keys())[0]
    subject_server = list((student_dict[name]['scores']).keys())
    #print(subject_client)
    #print(subject_server)
    for subject,score in data['scores'].items():
        subject_dict[subject] = score
    print(subject_dict)
    if subject_client not in subject_server:
        StudentInfoTable().insert_a_subject(student_id, subject, score )
    else:
        StudentInfoTable().update_a_subject(score, student_id, subject)
    student_dict1[name]  = {'name':name , 'scores':subject_dict}
    print(f"Modify {student_dict1[name]} success")
    student_dict1 = {**student_dict, **student_dict1}
    return student_dict1