#!/usr/bin/python3
"""This function queries the Reddit API and
returns the no of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """returns the no of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "J Agent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
