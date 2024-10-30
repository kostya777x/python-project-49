from brain_games.utils import get_random_number
from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game


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
    question = get_random_number()
    answer = is_prime(question)
    return answer, question


def run_prime():
    run_game(get_is_prime, PRIME_INSTRUCTION)
    return
