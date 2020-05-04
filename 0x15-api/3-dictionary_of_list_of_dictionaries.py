#!/usr/bin/python3
"""
Module for retreiving info from API
"""
import json
import requests
from sys import argv

json_dict = {}
user_id_list = []
users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
for user in users:
    user_id_list.append(user["id"])

for uid in user_id_list:
    dict_list = [] 
    url = "https://jsonplaceholder.typicode.com/users/{}/".format(uid)
    user = requests.get(url).json()["username"]
    tasks = requests.get(url + "todos/").json()
    for task in tasks:
        dict_list.append({"username": user, "task": task["title"], "completed": task["completed"]})
    json_dict.update({uid: dict_list})

obj = json.dumps(json_dict)


with open("todo_all_employees.json", "w") as file:
    file.write(obj)
