#!/usr/bin/python3
""" Module to request subreddit sub count """


def number_of_subscribers(subreddit):
    """ Return the number of subscribers of a subreddit """
    import requests
    import json
    from sys import argv

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "person_at_school"
    header = {'User-Agent': user_agent}
    resp = requests.get(url, headers=header, allow_redirects=False)
    if (resp.status_code != 200):
        return 0
    else:
        return(resp.json()['data']['subscribers'])
