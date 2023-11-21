#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""
import json
import requests


def export_all_employee_tasks_to_json():
    """Exports all tasks from all employees to JSON."""
    url = "https://jsonplaceholder.typicode.com"
    users_url = f"{url}/users"
    todos_url = f"{url}/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    user_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        task_list = []
        for todo in user_todos:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            task_list.append(task)
        user_tasks[user_id] = task_list

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    export_all_employee_tasks_to_json()
