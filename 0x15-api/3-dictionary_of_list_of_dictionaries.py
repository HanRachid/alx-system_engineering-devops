#!/usr/bin/python3
"""
gather data from api and structure and print it
"""
import json
import requests

rusers = requests.get("https://jsonplaceholder.typicode.com/users")
userresponse = rusers.json()
alluserdata = {}
for user in userresponse:
    rtodo = requests.get("https://jsonplaceholder.typicode.com/users/" +
                         str(user["id"]) + "/todos")
    USERNAME = user["username"]
    todoresponse = rtodo.json()
    USER_ID = user["id"]
    data = []
    for task in todoresponse:
        TASK_COMPLETED_STATUS = task["completed"]
        TASK_TITLE = task["title"]
        new_entry = {
            "username": USERNAME,
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
        }
        data.append(new_entry)
    alluserdata[USER_ID] = data

with open("todo_all_employees.json", "w", newline="") as json_file:
    json.dump(alluserdata, json_file)
