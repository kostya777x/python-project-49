import prompt
from brain_games.const import WELCOME, ANSWER_NAME


def welcome_user():
    print(WELCOME)
    name = prompt.string(ANSWER_NAME)
    print(f'Hello, {name}!')
    return name
