#!/usr/bin/python3
"""
gather data from api and structure and print it
"""
import json
import requests

rusers = requests.get("https://jsonplaceholder.typicode.com/users")
userresponse = rusers.json()

for user in userresponse:
    rtodo = requests.get("https://jsonplaceholder.typicode.com/users/" +
                         str(user["id"]) + "/todos")
    USERNAME = user["username"]
    todoresponse = rtodo.json()
    USER_ID = user["id"]
    data = {USER_ID: []}
    for task in todoresponse:
        TASK_COMPLETED_STATUS = task["completed"]
        TASK_TITLE = task["title"]
        new_entry = {
            "username": USERNAME,
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
        }
        data[USER_ID].append(new_entry)
    with open("todo_all_employees.json", "a", newline="") as json_file:
        json.dump(data, json_file)
