#!/usr/bin/env python3
from brain_games import utility
from brain_games.const import PRINT_YOUR_ANSWER, PRINT_PRIME
from brain_games.engine import engine
import prompt


def is_prime(number):
    answer = ''
    if number < 2:
        answer = 'no'
        return answer
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            answer = 'no'
            return answer
    answer = 'yes'
    return answer


def get_is_prime():
    number = utility.get_random()
    print(f'Question: {number}')
    answer_enter = prompt.string(PRINT_YOUR_ANSWER)
    answer = is_prime(number)
    return answer, answer_enter


def run_is_prime():
    engine(get_is_prime, PRINT_PRIME)
    return
