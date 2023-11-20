#!/usr/bin/python3
import csv
import requests
import sys


def todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(base_url, employee_id)).json()
    todos = requests.get('{}/todos?userId={}'
                         .format(base_url, employee_id)).json()

    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user['username'],
                             task['completed'], task['title']])


if __name__ == "__main__":
    todo_list_progress(int(sys.argv[1]))
