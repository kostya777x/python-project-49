#!/usr/bin/env python3
from brain_games import cli
from random import randint
import prompt


def progression():
    len = randint(5, 15)
    progression_list = [randint(1, 50)]
    diff = randint(1, 10)
    i = 0
    while i < len:
        progression_list.append(progression_list[i] + diff)
        i += 1
    return progression_list


def progression_number(name):
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        progression_list = progression()
        char = randint(0, (len(progression_list) - 1))
        answer = str(progression_list[char])
        progression_list[char] = '..'
        result = " ".join(map(str, progression_list))
        print(f'Question: {result}')
        answer_enter = prompt.string('Your answer: ')
        if answer != answer_enter:
            return (print("{}".format(answer_enter), 'is wrong answer ;(. '
                          'Correct answer was', "{}".format(answer + "."),
                          "\nLet's try again,", "{}".format(name + "!)")))
        else:
            print('Correct!')
            i += 1
    return (print(f'Congratulations, {name}!'))


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(f'Hello, {name}!')
    progression_number(name)


if __name__ == '__main__':
    main()
