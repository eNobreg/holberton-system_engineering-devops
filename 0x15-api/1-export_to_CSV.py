#!/usr/bin/python3
"""
Module for retreiving info from API
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1])
    user = requests.get(url).json()["username"]
    tasks = requests.get(url + "todos/").json()
    with open("{}.csv".format(argv[1]), mode='w') as file:
        write_file = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            write_file.writerow([argv[1], user, task["completed"], task["title"]])
