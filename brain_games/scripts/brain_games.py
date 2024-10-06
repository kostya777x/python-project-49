#!/usr/bin/env python3
from brain_games import cli
from brain_games.scripts import brain_even
from brain_games.scripts import brain_calc


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}!')
    brain_even.even_number(name)
    brain_calc.calc_number(name)


if __name__ == '__main__':
    main()
