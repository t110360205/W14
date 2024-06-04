from Add import Add
from Print import Print
from Query import Query
from Del import Del
from Modify import Modify
import socket
import json
BUFFER_SIZE = 1940
host = "127.0.0.1"
port = 20001
select={
    'add':Add,
    "show":Print,
    'query':Query,
    'delete':Del,
    'modify':Modify
}
#message={"command": "add", "parameters": {"name": "Test2", "scores": {"Python": 15,"er":50.0}}}
#message={"command": "show", "parameters": {}}
#message={"command": "query", "parameters": {"name": "Test"}} 
#message={'command': 'delete', 'parameters': {'name': 'Test2'}}
#message={'command': 'Add', 'parameters': {'name': 'Test2', 'scores_dict': {'Python': 16.0, 'er': 500.0,"eeee":50.0}}}

reply_msg = select[message['command']](message).indata()