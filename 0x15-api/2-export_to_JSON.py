#!/usr/bin/python3
"""Export user data to JSON"""

import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    username = requests.get(user_url).json().get('username')

    tasks_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks = requests.get(tasks_url).json()

    # Create JSON structure
    user_tasks = [{

         user_tasks = [{
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": username
                  } for task in tasks]
    user_data = {user_id: user_tasks}

    with open(f'{user_id}.json', 'w') as file:
        json.dump(user_data, file)
