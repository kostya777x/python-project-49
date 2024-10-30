from brain_games import utils
from random import randint
from brain_games.consts import PRINT_PROGRESSION, MIN_PROGRESSION_LEN, \
    MAX_PORGRESSION_LEN
from brain_games.engine import run_game
import prompt


def get_progression_with_skip():
    start_progression = utils.get_random_number()
    diff_progtression = utils.get_random_number()
    len_progression = randint(MIN_PROGRESSION_LEN, MAX_PORGRESSION_LEN)
    char = randint(0, (len_progression - 1))
    progression_list = []
    for i in range(len_progression):
        progression_list.append(start_progression + diff_progtression * i)
    answer = str(progression_list[char])
    progression_list[char] = '..'
    progression_list_with_skip = " ".join(map(str, progression_list))
    return progression_list_with_skip, answer


def get_progression_skip_number():
    progression_list_with_skip, answer = get_progression_with_skip()
    print(f'Question: {progression_list_with_skip}')
    answer_enter = prompt.string('Your answer: ')
    return answer, answer_enter


def run_get_progression_number():
    run_game(get_progression_skip_number, PRINT_PROGRESSION)
    return
