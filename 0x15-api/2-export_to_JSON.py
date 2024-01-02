#!/usr/bin/python3
"""
gather data from api and structure and print it
"""
import json
import requests
import sys

if len(sys.argv) == 2:
    ruser = requests.get("https://jsonplaceholder.typicode.com/users/" +
                         sys.argv[1] + "/")
    userresponse = ruser.json()
    rtodo = requests.get("https://jsonplaceholder.typicode.com/users/" +
                         sys.argv[1] + "/todos")
    USERNAME = userresponse["username"]
    todoresponse = rtodo.json()
    USER_ID = userresponse["id"]
    data = {USER_ID: []}
    for task in todoresponse:
        TASK_COMPLETED_STATUS = str(task["completed"])
        TASK_TITLE = task["title"]
        new_entry = {
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        }
        data[USER_ID].append(new_entry)
    with open("{}.json".format(sys.argv[1]), "w", newline="") as json_file:
        json.dump(data, json_file)
