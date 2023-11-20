#!/usr/bin/python3
"""
    Python script that gathers data from the
    provided REST API
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) < 2:
        exit()

    completed_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
        .format(argv[1]))
    completed_tasks = completed_tasks.json()

    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}"
        .format(argv[1]))
    employee_name = employee_name.json()
    employee_name = employee_name[0]["name"].ljust(20)

    remaining_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    remaining_tasks = len(remaining_tasks.json())

    completed_list = []
    for task in completed_tasks:
        completed_list.append("\t {}".format(task["title"]))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), remaining_tasks))

    for task in completed_list:
        print(task)
