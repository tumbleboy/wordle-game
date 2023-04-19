# MAIN PROJECT FILE. UPDATE AS I GO ALONG. JARRED OSBORNE, PROGRAMMING CERT 4

import random

# Open the file and create list of words
open_file = open("target_words.txt", "r")
target_words = open_file.read().splitlines()


# Choose random word from list of words
def get_target_word():
    return random.choice(target_words)


# Print a greeting to the user
def greeting():
    print("*** Welcome to WORDLE. ***\n"
          "You have 6 attempts to guess the 5 letter word.\n"
          "Good luck!")


# Get input from user
def get_user_word():
    return input("What is the 5 letter word?: ")


# Function that runs the sequence of instructions
def main_game():
    greeting()
    attempts = 6
    target_word = get_target_word()
    print(target_word)
    while True:
        result = ["_"]*5
        user_word = get_user_word()
        # Score guess
        for position in range(len(user_word)):
            if user_word[position] == target_word[position]:
                result[position] = target_word[position]
            # If the letter is in the word but incorrect space
            elif user_word[position] in target_word:
                result[position] = "*"

        # If the letter is not in the word
        for position in range(len(user_word)):
            if user_word[position] is not target_word[position]:
                continue
        # Checks if user has run out of attempts or the word has been guessed.
        if attempts == 0:
            print("You lose")
            break
        elif target_word == user_word:
            print("Congrats you guessed the word! it was", "".join(target_word).upper())
            break
        print(result)
        attempts = attempts - 1


main_game()
