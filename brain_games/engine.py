import prompt
from brain_games.consts import ROUND


def run_game(get_answer_and_question, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(instruction)
    for _ in range(ROUND):
        answer, question = get_answer_and_question()
        print(f'Question: {question}')
        answer_enter = prompt.string('Your answer: ')
        if answer != answer_enter:
            return (print(f"{answer_enter} is wrong answer ;(. "
                          f"Correct answer was {answer}."
                          f"\nLet's try again, {name}!)"))
        else:
            print('Correct!')
    return (print(f'Congratulations, {name}!'))
