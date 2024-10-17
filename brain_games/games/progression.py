#!/usr/bin/env python3
from brain_games import utility
from random import randint
from brain_games.const import PRINT_PROGRESSION, MIN_PROGRESSION_LEN, \
    MAX_PORGRESSION_LEN, PRINT_YOUR_ANSWER
from brain_games.engine import engine
import prompt


def get_progression_with_skip():
    start_progression = utility.get_random()
    diff_progtression = utility.get_random()
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
    answer_enter = prompt.string(PRINT_YOUR_ANSWER)
    return answer, answer_enter


def run_get_progression_number():
    engine(get_progression_skip_number, PRINT_PROGRESSION)
    return
