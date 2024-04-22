"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Simona Menšíková
email: simensikova@gmail.com
discord: mensikxs@gmail.com
"""
import os
import random
import time


def main_game():
    separator = 47 * "-"
    secret_number = generate_number()
    guesses = 0

    clear_screen()
    welcome_player()
    print(secret_number)

    while True:
        start = time.time()
        entered_number = validate_number()
        matched_numbers = count_matched_numbers(entered_number, secret_number)
        bulls = count_matched_positions(entered_number, secret_number)
        cows = count_cows(matched_numbers, bulls)
        guesses += 1

        if entered_number == secret_number:
            end = time.time()
            congratulation(guesses)
            print(separator)
            save_score(guesses)
            average = average_score()
            score_validation(guesses, average)
            print(separator)
            print(f"Average number of guesses: {average:.3}")
            print(separator)
            count_time(start, end)
            break
        else:
            show_score(bulls, cows)
            continue

def clear_screen() -> None:
    """Clears the console window for both Windows and Unix-like systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_player() -> None:
    separator = 47 * "-"
    print(
        "Hi there!",
        separator,
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.",
        separator,
        "Enter a 4 digit number: ",
        sep= "\n"
    )

def generate_number() -> list:
    secret_number = []
    first_number = random.randint(1, 9)
    secret_number.append(str(first_number))

    while len(secret_number) != 4:  
        other_number = random.randint(0, 9)
        if str(other_number) not in secret_number:
            secret_number.append(str(other_number))
    return secret_number

def validate_number() -> list:
    separator = 47 * "-"
    number = []

    while True:
        print(separator)
        choice = input(">>> ")
        if not choice.isnumeric():
            print("Please enter only numeric symbols..")
        elif len(choice) != 4:
            print("Please enter a 4 digit number..")
        elif choice[0] == "0":
            print("Number can't start with 0..")
        elif len(set(choice)) != len(choice):
            print("Please enter a number with unique digits..")
        else:
            number = list(choice)
            break
    return number

def count_matched_numbers(entered_number: list, secret_number: list) -> int:
    matched_numbers = set(entered_number).intersection(set(secret_number))
    return len(matched_numbers)

def count_matched_positions(entered_number: list, secret_number: list) -> int:
    matched_positions = 0 #bulls
    for index in range(len(entered_number)):
        if entered_number[index] == secret_number[index]:
            matched_positions += 1
    return matched_positions#bulls

def count_cows(matched_numbers, matched_positions) -> int:
    cows = matched_numbers - matched_positions
    return cows
    
def show_score(bulls: int, cows: int) -> None:
    if bulls == 1:
        bull_number = "bull"
    else:
        bull_number = "bulls"

    if cows == 1:
        cows_number = "cow"
    else:
        cows_number = "cows"
    
    print(f"{bulls} {bull_number}, {cows} {cows_number}")

def save_score(guesses: int) -> None:
    with open("score_statistics.txt", "a") as file:
        file.writelines(f"{guesses}")

def average_score() -> int:
    count = 0
    with open("score_statistics.txt", "r") as file:
        statistic = file.readlines()
        for number in statistic:
            
            count += int(number)
    average = count / len(statistic)
    return average

def score_validation(guesses: int, average: int) -> None:
    if guesses < average:
        print("That's amazing!")
    elif abs(guesses-average) <= 0.59:
        print("That's average.")
    else:
        print("That's not so good.")

def congratulation(guesses: int) -> None:
    if guesses == 1:
        print(f"Correct, you've guessed the right number\nin {guesses} guess!")
    else:
        print(f"Correct, you've guessed the right number\nin {guesses} guesses!")

def count_time(start, end) -> None:
    time = end - start
    print(f"Length of your game: {time:.3} seconds\n")


if __name__ == "__main__":
    main_game()
