#!/usr/bin/python3
"""Export all user data to JSON"""

import json
import requests

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    
    # Fetch all users
    users = requests.get(base_url).json()
    
    all_users_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        
        # Fetch tasks for each user
        tasks_url = f'{base_url}{user_id}/todos/'
        tasks = requests.get(tasks_url).json()
        
        # Prepare task data
        user_tasks = [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            for task in tasks
        ]
        
        all_users_tasks[user_id] = user_tasks
    
    # Write all user data to JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_users_tasks, file)

