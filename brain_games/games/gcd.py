from brain_games import utils
import math
from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import run_game
import prompt


def search_gcd(number_1, number_2):
    gcd = math.gcd(number_1, number_2)
    return gcd


def get_gcd():
    number_1 = utils.get_random_number()
    number_2 = utils.get_random_number()
    print(f'Question: {number_1} {number_2}')
    answer_enter = prompt.string('Your answer: ')
    answer = str(search_gcd(number_1, number_2))
    return answer, answer_enter


def run_get_gcd():
    run_game(get_gcd, GCD_INSTRUCTION)
    return
