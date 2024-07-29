#!/usr/bin/python3
"""CSV Export Script"""

import requests
import sys
import csv

if __name__ == '__main__':
    user_id = sys.argv[1]

    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    username = requests.get(user_url).json().get('username')

    # Fetch tasks
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks = requests.get(tasks_url).json()

    # Write to CSV
    with open(f'{user_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows([[user_id, username, task['completed'], task['title']] for task in tasks])

