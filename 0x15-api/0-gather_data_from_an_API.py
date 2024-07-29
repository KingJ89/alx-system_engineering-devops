#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    # API base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Get user info
    user = requests.get(f"{url}users/{sys.argv[1]}").json()
    todos = requests.get(f"{url}todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks
    completed = [t["title"] for t in todos if t["completed"]]

    print(f"Employee {user['name']} is done with tasks({len(completed)}/{len(todos)}):")

    # Print completed task titles
    for task in completed:
        print(f"\t {task}")
