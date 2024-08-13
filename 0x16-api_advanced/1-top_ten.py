#!/usr/bin/python3

import requests

def display_top_ten_posts(subreddit):

    # Construct the Reddit API endpoint URL
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define a custom User-Agent to prevent request rate limiting
    headers = {'User-Agent': 'JanYayaBot 1.0'}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(api_url, headers=headers, allow_redirects=False)

        # Verify that the request was successful
        if response.status_code == 200:
            # Extract and print the titles of the top 10 hot posts
            posts = response.json().get('data', {}).get('children', [])
            for index, post in enumerate(posts[:10]):
                print(f"{index + 1}: {post.get('data', {}).get('title', 'No Title')}")
        else:
            # Handle cases where the request was not successful
            print("Unable to fetch posts.")
    except requests.RequestException as e:
        # Catch and handle any exceptions during the request
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    display_top_ten_posts("example_subreddit")

