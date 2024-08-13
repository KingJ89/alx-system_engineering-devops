#!/usr/bin/python3
"""Querying Reddit for the number of subscribers of a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Query a subreddit and retrieve the number of subscribers."""
    
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and not redirected
        if response.status_code == 200:
            # Parse JSON response to extract the number of subscribers
            data = response.json().get('data', {})
            sub_count = data.get('subscribers', 0)
            return sub_count
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
