#!/usr/bin/python3
"""
Returns the number of subscribers in a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """returns the numbers of subscribers in a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit), headers={'User-Agent': '0x16-api_advanced:project'}).json()
    subs = r.get("data",{}).get("subscribers",0)
    return subs
