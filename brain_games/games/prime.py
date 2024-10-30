from brain_games import utils
from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game
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
    number = utils.get_random_number()
    print(f'Question: {number}')
    answer_enter = prompt.string('Your answer: ')
    answer = is_prime(number)
    return answer, answer_enter


def run_is_prime():
    run_game(get_is_prime, PRIME_INSTRUCTION)
    return
