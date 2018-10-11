import random


def generate_answer():
    possible_answers = ["apple", "orange", "lemon", "banana", "grape", "pineapple", "cherry"]
    index = random.randrange(0, len(possible_answers))
    return possible_answers[index]


def start_game():
    name = input("Great! Enter your name: ")
    print(f"Hello, {name.capitalize()}. Let's start the game now.")

    given_answer = generate_answer()
    user_answer = list(given_answer)
    wrong_attempts = 0
    attempts_left = 10
    word = []
    for i in user_answer:
        word.append("_")
    while user_answer != word:
        letter = input(f"Enter your letter: {user_answer}")
        if len(letter) > 1:
            print("that's more than a letter! try again.")
        if letter in user_answer:
            for ind in range(0, len(user_answer)):
                if user_answer[ind] == letter:
                    word[ind] = letter
            print(word)
        else:
            wrong_attempts += 1
            print(f"oops, there is no such letter in the word! You have {attempts_left - wrong_attempts}"
                  f" attempts left.")
        if wrong_attempts >= 10:
            print(f"Game over. it was {str}")
            break
    if user_answer == word:
        print("You won!")


answer = input("If you wanna start the game, enter 1. If not, press any other button: \n")
try:
    if int(answer) == 1:
        start_game()
    else:
        raise ArithmeticError
except ValueError:
    print("Doesn't look like a number to me.")
except ArithmeticError:
    print("Well, goodbye then!")