def add_sever(message, student_dict):
    student_dict1 = dict()
    subject_dict = dict()
    data = message['parameters']
    name = data['name']
    for subject,score in data['scores'].items():
        subject_dict[subject] = score

    student_dict1[name]  = {'name':name , 'scores':subject_dict}
    print(f"ADD {student_dict1[name]} success")
    student_dict1 = {**student_dict, **student_dict1}
    return student_dict1