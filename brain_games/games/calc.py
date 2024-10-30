from brain_games import utils
from brain_games.consts import CALC_INSTRUCTION, OPERATOR_LIST
from brain_games.engine import run_game
import prompt
import random


def search_expression_result(number_1, number_2, operator):
    expression = f'{number_1}{operator}{number_2}'
    answer = eval(expression)
    return answer


def get_expression_result():
    number_1, number_2 = utils.get_random_number(), utils.get_random_number()
    operator = random.choice(OPERATOR_LIST)
    print(f'Question: {number_1} {operator} {number_2}')
    answer_enter = prompt.string('Your answer: ')
    answer = str(search_expression_result(number_1, number_2, operator))
    return answer, answer_enter


def run_get_expression_result():
    run_game(get_expression_result, CALC_INSTRUCTION)
    return
