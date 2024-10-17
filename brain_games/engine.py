#!/usr/bin/env python3
from brain_games import cli
from brain_games.const import ROUND


def engine(get_answer_and_answer_enter, instruction):
    name = cli.welcome_user()
    print(instruction)
    i = 0
    while i < ROUND:
        answer, answer_enter = get_answer_and_answer_enter()
        if answer != answer_enter:
            return (print("{}".format(answer_enter), 'is wrong answer ;(. '
                          'Correct answer was', "{}".format(answer + "."),
                          "\nLet's try again,", "{}".format(name + "!)")))
        else:
            print('Correct!')
            i += 1
    return (print(f'Congratulations, {name}!'))
