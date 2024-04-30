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
    """
    Main function for the bulls and cows game.

    Runs the main game loop, allowing the player to guess the secret number.
    Displays game information, including scores and time taken.
    """
    separator = 47 * "-"
    secret_number = generate_number()
    guesses = 0

    clear_screen()
    welcome_player()

    while True:
        start = time.time()
        entered_number = validate_number()
        matched_numbers = count_matched_numbers(entered_number, secret_number)
        bulls = count_matched_positions(entered_number, secret_number)
        cows = count_cows(matched_numbers, bulls)
        guesses += 1

        if entered_number != secret_number:
            display_score(bulls, cows)
            continue
        else:
            end = time.time()
            congratulation(guesses)
            print(separator)
            save_score(guesses)
            average = count_average_score()
            score_validation(guesses, average)
            print(separator)
            display_average_score(average)
            print(separator)
            count_time(start, end)
            break


def clear_screen() -> None:
    """
    Clears the console window for both Windows and Unix-like
    systems.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_player() -> None:
    """
    Prints a welcome message and instructions for a bulls and
    cows game.
    Prompts the player to enter a 4-digit number.
    """
    separator = 47 * "-"
    print(
        "Hi there!",
        separator,
        "I've generated a random 4 digit number for you.",
        "Let's play a bulls and cows game.",
        separator,
        "Enter a 4 digit number: ",
        sep="\n",
    )


def generate_number() -> list:
    """
    Generates a random 4-digit number with unique digits.

    Returns:
        list: A list containing four unique digits as strings.
    """
    secret_number = []
    first_number = random.randint(1, 9)
    secret_number.append(str(first_number))

    while len(secret_number) != 4:
        other_number = random.randint(0, 9)
        if str(other_number) not in secret_number:
            secret_number.append(str(other_number))
    return secret_number


def validate_number() -> list:
    """
    Validates user input for a 4-digit number.

    Prompts the user to input a 4-digit number until a valid input
    is received.
    Valid input is a 4-digit number with unique digits and no
    leading zero.

    Returns:
        list: A list containing the validated 4-digit number
        as individual digits.
    """
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
            print("The number must not start with 0..")
        elif len(set(choice)) != len(choice):
            print("Please enter a number with unique digits..")
        else:
            number = list(choice)
            break
    return number


def count_matched_numbers(
        entered_number: list,
        secret_number: list) -> int:
    """
    Counts the number of matched digits between the entered number and
    the secret number.

    Parameters:
        entered_number (list): A list of digits entered by the player.
        secret_number (list): A list of digits representing the secret
        number.

    Returns:
        int: The count of matched digits between the entered and secret
        number.
    """
    matched_numbers = set(entered_number).intersection(set(secret_number))
    return len(matched_numbers)


def count_matched_positions(
        entered_number: list,
        secret_number: list) -> int:
    """
    Counts the number of digits in the entered number that match both
    in value and position with digits in the secret number.

    Parameters:
        entered_number (list): A list of digits entered by the player.
        secret_number (list): A list of digits representing the secret
        number.

    Returns:
        int: The count of matched digits in both value and position
        between the entered and secret number.
    """
    matched_positions = 0  # bulls
    for index in range(len(entered_number)):
        if entered_number[index] == secret_number[index]:
            matched_positions += 1
    return matched_positions  # bulls


def count_cows(
        matched_numbers: int,
        matched_positions: int) -> int:
    """
    Counts the number of cows in the bulls and cows game.

    Parameters:
        matched_numbers (int): The count of matched digits between
        the entered and secret number (excluding positions).
        matched_positions (int): The count of digits that match both
        in value and position between the entered and secret number.

    Returns:
        int: The count of cows in the game, calculated as the difference
        between matched_numbers and matched_positions.
    """
    cows = matched_numbers - matched_positions
    return cows


def display_score(bulls: int, cows: int) -> None:
    """
    Displays the score of bulls and cows in the game with distinction
    between singular and plural forms.

    Parameters:
        bulls (int): The number of bulls.
        cows (int): The number of cows.
    """
    bull_number = "bull"
    cow_number = "cow"

    if bulls != 1:
        if cows != 1:
            bull_number = "bulls"
            cow_number = "cows"
        else:
            bull_number = "bulls"
    print(f"{bulls} {bull_number}, {cows} {cow_number}")


def save_score(guesses: int) -> None:
    """
    Appends the number of guesses to a file for score statistics.

    Parameters:
        guesses (int): The total number of guesses made by the player.
    """
    with open("score_statistics.txt", "a") as file:
        file.writelines(f"{guesses} ")


def count_average_score() -> int:
    """
    Calculates the average score from saved score statistics.
    Reads the score statistics from a txt file and calculates
    the average number of guesses in bulls and cows game.

    Returns:
        int: The average number of guesses.
    """
    count = 0
    with open("score_statistics.txt", "r") as file:
        reader = file.readlines()
        statistics = reader[0].split()
        for number in statistics:
            count += int(number)
    average = count / len(statistics)
    return average


def display_average_score(average: int) -> None:
    """
    Displays the average number of guesses.

    Parameters:
        average (int): The average number of guesses to be displayed.
    """
    print(f"Average number of guesses: {average:.3}")


def score_validation(guesses: int, average: int) -> None:
    """
    Validates the player's score against the average score.

    Parameters:
        guesses (int): The number of guesses made by the player.
        average (int): The average number of guesses.
    """
    if guesses < average:
        print("That's amazing!")
    elif abs(guesses - average) <= 0.5:
        print("That's average.")
    else:
        print("That's not so good.")


def congratulation(guesses: int) -> None:
    """
    Congratulates the player on guessing the right number
    and displays the number of guesses made.

    Parameters:
        guesses (int): The number of guesses made by the player.
    """
    if guesses == 1:
        print(
            f"Correct, you've guessed the right number\nin {guesses} guess!"
        )
    else:
        print(
            f"Correct, you've guessed the right number\nin {guesses} guesses!"
        )


def count_time(start, end) -> None:
    """
    Calculates and displays the length of the game in seconds.

    Parameters:
        start: The start time of the game.
        end: The end time of the game.
    """
    time = end - start
    print(f"Length of your game: {time:.4} seconds\n")


if __name__ == "__main__":
    main_game()
