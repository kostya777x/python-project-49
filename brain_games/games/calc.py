from brain_games.utils import get_random_number
from brain_games.consts import CALC_INSTRUCTION
from brain_games.engine import run_game
import random


def search_expression_result(operator, number_1, number_2):
    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2


def get_expression_result():
    number_1, number_2 = get_random_number(), get_random_number()
    operator = random.choice(['+', '-', '*',])
    question = f'{number_1}{operator}{number_2}'
    answer = str(search_expression_result(operator, number_1, number_2))
    return answer, question


def run_calc():
    run_game(get_expression_result, CALC_INSTRUCTION)
