#!/usr/bin/env python3
from brain_games import cli
from random import randint
import prompt


def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def gcd_number(name):
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        print(f'Question: {number_1} {number_2}')
        answer_enter = prompt.string('Your answer: ')
        answer = str(gcd(number_1, number_2))
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
    gcd_number(name)


if __name__ == '__main__':
    main()
