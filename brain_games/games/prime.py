from brain_games.utils import get_random_number
from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_prime(number):
    if number < 2:
        return True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_is_prime():
    question = get_random_number()
    answer = 'yes' if is_prime(question) else 'no'
    return answer, question


def run_prime():
    run_game(get_is_prime, PRIME_INSTRUCTION)
    return
