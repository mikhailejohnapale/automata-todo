import sys
from pytodoist import todoist


user = todoist.login('firstnamelastname@gmail.com', 'secret_password')
project = user.get_project('Automata')

tasks = project.get_tasks()
for task in tasks:
    print(task.content)
