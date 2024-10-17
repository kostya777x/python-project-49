#!/usr/bin/env python3
from random import randint
from brain_games.const import FIRST_RANDOM_NUMBER, SECOND_RANDOM_NUMBER


def get_random():
    number = randint(FIRST_RANDOM_NUMBER, SECOND_RANDOM_NUMBER)
    return number
