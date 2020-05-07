#!/usr/bin/python3
""" Module to request subreddit hot posts """

def top_ten(subreddit):
	""" Return the number hot posts """
	import requests
	import json
	from sys import argv

	url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
	user_agent = "person_at_school"
	header = {'User-Agent': user_agent}
	resp = requests.get(url, headers=header, allow_redirects=False, params={'limit': 10})
	if (resp.status_code == 302):
		print('None')
	else:
		data = resp.json()["data"]
		children = data['children']
		for entry in children:
			print(entry['data']['title'])