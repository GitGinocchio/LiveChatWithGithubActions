from jinja2 import Environment, FileSystemLoader
import requests
import os

env = Environment(loader=FileSystemLoader('templates'))

GITHUB_REPOSITORY = os.environ['GITHUB_REPOSITORY']
GITHUB_ISSUE_NUMBER = os.environ['GITHUB_ISSUE_NUMBER']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

comments = requests.get(
    f"https://api.github.com/repos/{GITHUB_REPOSITORY}/issues/{GITHUB_ISSUE_NUMBER}/comments",
    headers={
        #"Authorization": f"token {GITHUB_TOKEN}",
        "Accept" : "application/vnd.github.v3+json"
        }
    ).json()

print(comments)

template = env.get_template('chat-v1.svg')

content = template.render(messages=[
    ("User","Messaggio 1"),
    ("User","Messaggio 2"),
    ("User","Messaggio 3"),
    ("User","Messaggio 4"),
    ("User","Messaggio 5"),
    ("User","Messaggio 6"),
    ("User","Messaggio 7"),
    ("User","Messaggio 8"),
    ("User","Messaggio 9")
])

#with open("chat-v1.svg","w") as f:
    #f.write(content)