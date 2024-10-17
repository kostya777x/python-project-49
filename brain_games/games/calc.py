#!/usr/bin/env python3
from brain_games import utility
from brain_games.const import PRINT_YOUR_ANSWER, PRINT_CALC, OPERATOR_LIST
from brain_games.engine import engine
import prompt
import random


def search_expression_result(number_1, number_2, operator):
    expression = f'{number_1}{operator}{number_2}'
    answer = eval(expression)
    return answer


def get_expression_result():
    number_1, number_2 = utility.get_random(), utility.get_random()
    operator = random.choice(OPERATOR_LIST)
    print(f'Question: {number_1} {operator} {number_2}')
    answer_enter = prompt.string(PRINT_YOUR_ANSWER)
    answer = str(search_expression_result(number_1, number_2, operator))
    return answer, answer_enter


def run_get_expression_result():
    engine(get_expression_result, PRINT_CALC)
    return
