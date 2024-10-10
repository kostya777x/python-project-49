#!/usr/bin/env python3
from brain_games import cli
from random import randint
import prompt


def is_prime(number):
    n = 2
    while number % n != 0:
        n += 1
    return n == number


def prime_number(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(1, 20)
        answer = 'no'
        if is_prime(number) is True:
            answer = 'yes'
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
    prime_number(name)


if __name__ == '__main__':
    main()
