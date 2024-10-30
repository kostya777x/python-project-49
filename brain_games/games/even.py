from brain_games import utils
from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game
import prompt


def is_even(number):
    return number % 2 == 0


def get_even():
    number = utils.get_random_number()
    if is_even(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    print(f'Question: {number}')
    answer_enter = prompt.string('Your answer: ')
    return answer, answer_enter


def run_get_even():
    run_game(get_even, EVEN_INSTRUCTION)
