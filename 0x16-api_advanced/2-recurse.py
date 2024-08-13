#!/usr/bin/python3
"""Recursive Reddit API Query for Hot Articles Titles."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Retrieve hot post titles from a subreddit using Reddit API.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): Accumulates the titles of hot posts.
        after (str): Pagination token to fetch the next set of results.

    Returns:
        list: Titles of hot articles if successful, otherwise None.
    """
    # Construct URL for the Reddit API endpoint with subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent for identification with Reddit API
    headers = {
        "User-Agent": "python:reddit.api.hotlist:v1.0.0 (by /u/yourusername)"
    }

    # Parameters for API request to control pagination and limit
    params = {
        "after": after,
        "limit": 100
    }

    # Execute GET request to Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if subreddit not found or request fails
    if response.status_code != 200:
        return None

    # Extract JSON data from the response
    data = response.json().get("data", {})

    # Update pagination token from response
    after = data.get("after")

    # Append each hot post title to the collected titles list
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    # If there is a next page, recurse to fetch additional titles
    if after is not None:
        return recurse(subreddit, hot_list, after)

    # Return the accumulated list of hot post titles
    return hot_list
