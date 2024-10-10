#!/usr/bin/env python3
from brain_games import cli
from random import randint
import random
import prompt


def calc_number(name):
    print('What is the result of the expression?')
    i = 0
    operator_list = ['+', '-', '*',]
    while i < 3:
        operator = random.choice(operator_list)
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        if operator == '+':
            answer = number_1 + number_2
        elif operator == '-':
            answer = number_1 - number_2
        elif operator == '*':
            answer = number_1 * number_2
        print(f'Question: {number_1} {operator} {number_2}')
        answer_enter = prompt.string('Your answer: ')
        if str(answer) != answer_enter:
            return (print("{}".format(answer_enter), 'is wrong answer ;(. '
                          'Correct answer was', "{}".format(str(answer) + "."),
                          "\nLet's try again,", "{}".format(name + "!)")))
        else:
            print('Correct!')
            i += 1
    return (print(f'Congratulations, {name}!'))


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}!')
    calc_number(name)


if __name__ == '__main__':
    main()
