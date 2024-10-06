from random import randint
import prompt


def progression():
    len = randint(5, 15)
    progression_list = [randint(1, 100)]
    diff = randint(1, 100)
    i = 0
    while i < len:
        progression_list.append(progression_list[i] + diff)
        i += 1
    return progression_list


def progression_number(name):
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        progression_list = progression()
        char = randint(0, (len(progression_list) - 1))
        answer = str(progression_list[char])
        progression_list[char] = '..'
        print(f'Question: {progression_list}')
        answer_enter = prompt.string('Your answer: ')
        if answer != answer_enter:
            return (print(f"'{answer_enter}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!)"))
        else:
            print('Correct!')
            i += 1
    return (print(f'Congratulations, {name}!'))
