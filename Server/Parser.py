from command.AddStu import AddStu
from command.DelStu import DelStu
from command.ModifyStu import ModifyStu
from command.PrintAll import PrintAll
from command.QueryStu import QueryStu

action_list = {
    "query": QueryStu,
    "add": AddStu, 
    "delete": DelStu, 
    "modify": ModifyStu, 
    "show": PrintAll
}

class Parser():
    def __init__(self, data):
        self.student_dict = data
        # pass
    
    def execute(self, command,data):
        reply_msg = dict()
        try :
            reply_msg =  action_list[command](self.student_dict, data).execute()
            
        except Exception as e:
            print("parser error : ", e)

        return reply_msg