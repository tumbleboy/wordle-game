# MAIN PROJECT FILE. UPDATE AS I GO ALONG. JARRED OSBORNE, PROGRAMMING CERT 4

import random

# Open the file and create list of words
open_file = open("target_words.txt", "r")
target_words = open_file.read().splitlines()


# Choose random word from list of words
def get_target_word():
    return random.choice(target_words)


target_word = get_target_word()
result = []
print(target_word)


# Print a greeting to the user
def greeting():
    print("***Welcome to WORDLE.***\n"
          "You have 6 attempts to guess the 5 letter word.\n"
          "Good luck!")


greeting()


# Get input from user
def get_user_word():
    return input("What is the 5 letter word?: ")


user_word = list(get_user_word())


# Compare each character in user word with the target word
def score_guess():
    pass


score_guess()
print(result)
