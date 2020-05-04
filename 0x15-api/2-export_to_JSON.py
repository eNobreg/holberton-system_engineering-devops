#!/usr/bin/python3
"""
Module for retreiving info from API
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    dict_list = []
    json_dict = {}
    url = "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1])
    user = requests.get(url).json()["username"]
    tasks = requests.get(url + "todos/").json()
    for task in tasks:
        dict_list.append({"task": task["title"], "completed":
                         task["completed"],
                         "username": user})

    json_dict.update({argv[1]: dict_list})
    obj = json.dumps(json_dict)
    with open("{}.json".format(argv[1]), "w") as file:
        file.write(obj)
