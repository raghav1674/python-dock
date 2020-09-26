#!/bin/python3

print("content-type: text/json")
print()

import subprocess as sp
import cgi 
import json
import datetime

query = cgi.FieldStorage()


con_name = query.getvalue("con_name")


img_name = query.getvalue("image_name")


result=""


status,output = sp.getstatusoutput(f'sudo docker run -dit --name {con_name}  {img_name}')

if status == 0:
    result =json.dumps({
             "name" : str(con_name),
             "image" : str(img_name),
            "status": "started",
            'created_at': str(datetime.datetime.now())
             },indent=4)
else:
    result =json.dumps({
    "name" : str(con_name),
    "image" : str(img_name),
    "status": "exited",
    'tried_at': str(datetime.datetime.now()),
    "reason" : str(output)
            },indent=4)

print(result)

    






