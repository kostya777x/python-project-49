#!/usr/bin/env python3
from brain_games import utility
import math
from brain_games.const import PRINT_YOUR_ANSWER, PRINT_GCD
from brain_games.engine import engine
import prompt


def search_gcd(number_1, number_2):
    gcd = math.gcd(number_1, number_2)
    return gcd


def get_gcd():
    number_1 = utility.get_random()
    number_2 = utility.get_random()
    print(f'Question: {number_1} {number_2}')
    answer_enter = prompt.string(PRINT_YOUR_ANSWER)
    answer = str(search_gcd(number_1, number_2))
    return answer, answer_enter


def run_get_gcd():
    engine(get_gcd, PRINT_GCD)
    return
