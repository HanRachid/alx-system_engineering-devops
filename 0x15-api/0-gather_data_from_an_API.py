#!/usr/bin/python3
"""
gather data from api and structure and print it
"""
import sys

import requests

if len(sys.argv) == 2:
    ruser = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + sys.argv[1] + "/"
    )
    userresponse = ruser.json()
    rtodo = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + sys.argv[1] + "/todos"
    )
    EMPLOYEE_NAME = userresponse["name"]
    todoresponse = rtodo.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    DONE_TASKS = ""
    for task in todoresponse:
        TOTAL_NUMBER_OF_TASKS += 1
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            DONE_TASKS += "\t " + task["title"] + "\n"
    print(
        "Employee "
        + str(EMPLOYEE_NAME)
        + "is done with tasks ("
        + str(NUMBER_OF_DONE_TASKS)
        + "/"
        + str(TOTAL_NUMBER_OF_TASKS)
        + "):"
    )
    print(DONE_TASKS)
