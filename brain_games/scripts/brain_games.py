#!/usr/bin/env python3
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
