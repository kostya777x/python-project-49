#!/usr/bin/env python3
from brain_games import cli
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    cli.welcome_user(name)


if __name__ == '__main__':
    main()
