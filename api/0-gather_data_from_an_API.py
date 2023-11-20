#!/usr/bin/python3
""" Requests the user information from a given API """
import requests
import sys


def display_employee_progress(employee_id):
    """ script must display to stdout the employee todo list progress """
    url = "https://jsonplaceholder.typicode.com"
    empu = f"{url}/users/{employee_id}"
    todo = f"{url}/todos"

    emps = requests.get(empu).json()
    todos = requests.get(todo,
                         params={"userId": employee_id}).json()

    name = emps.get("name")
    if name is None:
        print(f"No employee found with ID {employee_id}")
        return

    complete = [t["title"] for t in todos if t["completed"]]
    done = len(complete)
    total = len(todos)

    print(f"Employee {name} is done with tasks({done}/{total}):")
    for task in complete:
        print(f"\t {task}")


if __name__ == "__main__":
    display_employee_progress(int(sys.argv[1]))
