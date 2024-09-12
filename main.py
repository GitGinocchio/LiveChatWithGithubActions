from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('templates'))

print("Comments:", os.environ['COMMENTS'])

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