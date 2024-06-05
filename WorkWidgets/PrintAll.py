class PrintAll:
    def __init__(self, student_dict):
        self.student_dict = student_dict


    def print(self, data_parameters):
        print ("\n==== student list ====\n")
        
        for key, val in data_parameters.items():
            print(f"Name: {key}")
            for subject, scr in val['scores'].items():
                    print(f" subject: {subject}, score: {scr}")
                      
        print ("======================") 
        return True
    def execute(self):
        return self.student_dict
