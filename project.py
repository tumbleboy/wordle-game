# MAIN PROJECT FILE. UPDATE AS I GO ALONG. JARRED OSBORNE, PROGRAMMING CERT 4

import random

# Open the file and create list of words
open_file = open("target_words.txt", "r")
target_words = open_file.read().splitlines()


# Choose random word from list of words
def get_target_word():
    return random.choice(target_words)


# Print a greeting to the user
def display_greeting():
    print("*** Welcome to WORDLE. ***\n"
          "You have 6 attempts to guess the 5 letter word.\n"
          "Good luck! type '/help' to display instructions.")


# Print help message
def display_help_message():
    print("Wordle is a game where you are to guess a random 5 letter word in 6 tries.\nAfter each guess the "
          "program will show you what letters are correct, correct but misplaced or not in the word at all.\n"
          "Correct letters will be shown in green, misplaced letters in yellow, and incorrect letters in grey.\n"
          "A useful tip: Try starting with a word that has common vowel combinations like AE, AI etc...")


# Get input from user
def get_user_word():
    while True:
        user_word = input("What is the 5 letter word?: ")
        # Checks if the user input is correct amount of letters.
        if len(user_word) > 5 or len(user_word) < 5:
            print("That's not 5 letters! Try again.")
            continue

        # Helpful commands
        elif user_word == "/help":
            display_help_message()
            continue
        elif user_word == "/quit":
            return user_word

        # Non existent words
        elif user_word not in target_words:
            print("That's not a real word! Try again.")
            continue
        else:
            return user_word


# Scoring algorithm
def score_guess(user_word, target_word, result):
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


# Function that runs the sequence of instructions
def play_game():
    display_greeting()
    attempts = 5
    target_word = get_target_word()
    print(target_word)

    # Beginning of gameplay loop.
    while True:
        result = ["_"]*5

        # Get input from user
        user_word = get_user_word()
        if user_word == "/quit":
            break

        # Scoring algorthm takes place here
        score_guess(user_word, target_word, result)

        # Checks if user has run out of attempts or the word has been guessed.
        if target_word == user_word:
            print("Congrats you guessed the word! it was", "".join(target_word).upper())
            break
        elif attempts == 0:
            print("You lose. The word was", "".join(target_word).upper())
            break

        # Print score at the end of each guess.
        print("".join(result))
        attempts = attempts - 1


play_game()
