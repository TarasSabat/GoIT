import os
import requests
import json


github_url = "https://api.github.com/user/repos"

token = os.getenv("GITHUB_TOKEN")

print(token)


headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {token}"
}

data = {
    "name": "Hello-World",
    "description": "This is your first repo!",
    "homepage": "https://github.com",
    "private": False
}


response = requests.get(github_url, headers=headers)

print(len(response.json()))


post_response = requests.post(
    url=github_url,
    headers=headers,
    data=json.dumps(data)
)

print(post_response.text)