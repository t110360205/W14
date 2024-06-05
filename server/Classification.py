from AddStu import AddStu
from PrintAll import PrintAll
from ModifyStu import ModifyStu
from DelStu import DelStu
from Query import Query
from AllStuName import AllStuName

class Classification:
    def __init__(self,data):
        self.data=data
    def execute(self):
        action_list = {
        "add": AddStu, 
        "show": PrintAll,
        "modify":ModifyStu,
        "delete":DelStu,
        "query":Query,
        "allname":AllStuName
        }
        try:
            reply=action_list[self.data['command']](self.data['parameters']).execute()
            return reply
        except Exception as e:
            print(e)