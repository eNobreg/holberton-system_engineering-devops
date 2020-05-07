#!/usr/bin/python3
""" Module to host a recursive function """


def recurse(subreddit, hot_list=[], after=''):
    """ recursive function """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "person_with_things"
    header = {"User-Agent": user_agent}
    resp = requests.get(url, headers=header, allow_redirects=False,
                        params={'after': after, 'limit': 100})
    if (resp.status_code != 200):
        return(None)
    else:
        data = resp.json()["data"]
        children = data["children"]
        for entry in children:
            hot_list.append(entry["data"]["title"])
        after = data["after"]

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
