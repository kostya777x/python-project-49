from brain_games.utils import get_random_number
from random import randint
from brain_games.consts import PROGRESSION_INSTRUCTION, MIN_PROGRESSION_LEN, \
    MAX_PORGRESSION_LEN
from brain_games.engine import run_game


def get_progression_with_skip():
    start_progression, diff_progtression = get_random_number(), \
        get_random_number()
    len_progression = randint(MIN_PROGRESSION_LEN, MAX_PORGRESSION_LEN)
    char = randint(0, (len_progression - 1))
    progression_list_with_skip = " ".join([
        '..' if i == char
        else str(start_progression + diff_progtression * i)
        for i in range(len_progression)
    ])
    answer = start_progression + diff_progtression * char
    return progression_list_with_skip, str(answer)


def get_progression_skip_number():
    question, answer = get_progression_with_skip()
    return answer, question


def run_progression():
    run_game(get_progression_skip_number, PROGRESSION_INSTRUCTION)
    return
