import random

def generate_number():
    number = random.randint(1, 100)
    return number

def start_the_game():
    print("Enter your guess: ")
    number = int(input())
    attempts = 10

    answer = generate_number()
    while answer != number:
        if attempts == 0:
            print(f"Game over, you lost. The correct answer was {answer}")
            break

        elif answer < number:
            print("Too low. Try again: ")
            number = int(input())
            attempts -= 1

        elif answer > number:
            print("Too high. Try again: ")
            number = int(input())
            attempts -= 1



        else:
            print(f"You won! It was {answer}")
            break


        print("Do you want to try again? Enter 'Y' for yes, 'N' for exit: ")

        final_answer = input()
        try:
            if final_answer.upper() == 'Y':
                start_the_game()
            elif final_answer.upper() == 'N':
                pass
        except ValueError:
            print("That's not a valid answer, but i'll take it as a no. See you!")


print("Welcome to the 'guess the number' game! Enter your name: ")
name = input()
print(f"Hello, {name.capitalize()}. Let's start now.")
start_the_game()

