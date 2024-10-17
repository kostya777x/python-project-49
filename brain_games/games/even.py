#!/usr/bin/env python3
from brain_games import utility
from brain_games.const import PRINT_EVEN, PRINT_YOUR_ANSWER
from brain_games.engine import engine
import prompt


def is_even(number):
    return number % 2 == 0


def get_even():
    number = utility.get_random()
    if is_even(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    print(f'Question: {number}')
    answer_enter = prompt.string(PRINT_YOUR_ANSWER)
    return answer, answer_enter


def run_get_even():
    engine(get_even, PRINT_EVEN)
