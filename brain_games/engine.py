import prompt
from brain_games.consts import ROUND


def run_game(get_answer_and_answer_enter, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(instruction)
    for _ in range(ROUND):
        answer, answer_enter = get_answer_and_answer_enter()
        if answer != answer_enter:
            return (print(f"{answer_enter} is wrong answer ;(. "
                          f"Correct answer was {answer}."
                          f"\nLet's try again, {name}!)"))
        else:
            print('Correct!')
    return (print(f'Congratulations, {name}!'))
