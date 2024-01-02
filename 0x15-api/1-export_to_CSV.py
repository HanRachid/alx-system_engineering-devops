#!/usr/bin/python3
"""
gather data from api and structure and print it
"""
import csv
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
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        for task in todoresponse:
            TASK_COMPLETED_STATUS = str(task["completed"])
            TASK_TITLE = task["title"]
            writer.writerow(
                [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
