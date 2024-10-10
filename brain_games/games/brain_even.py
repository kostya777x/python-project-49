#!/usr/bin/env python3
from brain_games import cli
from random import randint
import prompt


def even_number(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(1, 100)
        answer = ''
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print(f'Question: {number}')
        answer_enter = prompt.string('Your answer: ')
        if answer != answer_enter:
            return (print(answer_enter, ' is wrong answer ;(.'
                          'Correct answer was ', answer,
                          ".\nLet's try again, ", name, '!)'))
        else:
            print('Correct!')
            i += 1
    return (print(f'Congratulations, {name}!'))


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}!')
    even_number(name)


if __name__ == '__main__':
    main()
