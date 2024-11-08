from brain_games.utils import get_random_number
import math
from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import run_game


def get_gcd():
    number_1, number_2 = get_random_number(), get_random_number()
    question = f'{number_1} {number_2}'
    answer = str(math.gcd(number_1, number_2))
    return answer, question


def run_gcd():
    run_game(get_gcd, GCD_INSTRUCTION)
    return
