#!/usr/bin/python3
"""Yep"""
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def todo_list_progress(employee_id):
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    user = next((user for user in users if user['id'] == employee_id), None)
    if not user:
        print("User not found")
        return

    user_todos = [todo for todo in todos if todo['userId'] == employee_id]
    done_tasks = [todo for todo in user_todos if todo['completed']]

    print("Employee {} is done with tasks({}/{}):"
          .format(user['name'], len(done_tasks), len(user_todos)))

    for task in done_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    todo_list_progress(int(sys.argv[1]))
