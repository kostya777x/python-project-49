from brain_games.utils import get_random_number
from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game


def is_even(number):
    return number % 2 == 0


def get_even():
    question = get_random_number()
    answer = 'yes' if is_even(question) else 'no'
    return answer, question


def run_even_game():
    run_game(get_even, EVEN_INSTRUCTION)
