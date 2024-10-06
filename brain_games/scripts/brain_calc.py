from random import randint
import random
import prompt


def calc_number(name):
    print('What is the result of the expression?')
    i = 0
    operator_list = ['+', '-', '*',]
    while i < 3:
        operator = random.choice(operator_list)
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        if operator == '+':
            answer = number_1 + number_2
        elif operator == '-':
            answer = number_1 - number_2
        elif operator == '*':
            answer = number_1 * number_2
        print(f'Question: {number_1} {operator} {number_2} {answer}')
        answer_enter = prompt.string('Your answer: ')
        if str(answer) != answer_enter:
            return (print(f"'{answer_enter}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!)"))
        else:
            print('Correct!')
            i += 1
    return (print(f'Congratulations, {name}!'))
