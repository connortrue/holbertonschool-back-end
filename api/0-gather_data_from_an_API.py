#!/usr/bin/python3
"""Yep"""
import requests
import sys


def todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(base_url, employee_id)).json()
    todos = requests.get('{}/todos?userId={}'
                         .format(base_url, employee_id)).json()
    done_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):"
          .format(user['name'], len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    todo_list_progress(int(sys.argv[1]))
