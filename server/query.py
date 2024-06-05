def query(message , student_dict ):
    student_dict1 = dict()
    
    name = message['parameters']["name"]
    #print(student_dict["parameters"]["name"])
    #if name in message and name in student_dict:
    if name in student_dict .keys() :
        #name = message["name"]
        student_dict1['scores'] =  student_dict[name]["scores"]
        student_dict1['status'] = "OK"
        student_dict1["name"] = name
        return student_dict1
    else:
        student_dict1['status'] = "Fail"
        student_dict1['reason'] = 'The name is not found.'
        student_dict1["name"] = name
        return student_dict1
    