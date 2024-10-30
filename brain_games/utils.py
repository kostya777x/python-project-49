from random import randint
from brain_games.consts import FIRST_RANDOM_NUMBER, SECOND_RANDOM_NUMBER


def get_random_number():
    return randint(FIRST_RANDOM_NUMBER, SECOND_RANDOM_NUMBER)
