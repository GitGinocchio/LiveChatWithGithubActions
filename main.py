from jinja2 import Environment, FileSystemLoader
import requests

env = Environment(loader=FileSystemLoader('templates'))

comments = requests.get("https://api.github.com/repos/GitGinocchio/live-chat-with-github-actions/issues/comments").json()

messages = [(message['user']['login'],str(message['body']).strip()) for message in comments]

template = env.get_template('chat-v1.svg')

content = template.render(messages=messages)

with open("chat-v1.svg","w") as f:
    f.write(content)