import random

result = [" "] * 5
open_file = open("target_words.txt", "r")

# Create list of words
target_words = open_file.read().splitlines()
# print(target_words)
# for word in open_file:
#     target_words = open_file.readline().rstrip()
#     print(target_words)

# Get single word from list of target_words
word_to_find = random.choice(target_words)
print(word_to_find)


while True:
    user_word = input("Enter a 5 letter word: ")
    if user_word == "quit":
        break
    if len(user_word) < 5 or len(user_word) > 5:
        print("please enter a 5 letter word")
        continue
    if user_word not in target_words:
        print("That's not a real, word try again")
        continue
    # FIRST ALGORITHM
    for position in range(len(word_to_find)):
        if user_word[position] == word_to_find[position]:
            result[position] = word_to_find[position]
        # need to fix bug here involving user word with more identical letters than target word.
        elif user_word[position] in word_to_find:
            if user_word[position] is not word_to_find[position]:
                result[position] = "-"

    if word_to_find == user_word:
        print("Nice! you guessed the word. It was:", word_to_find.upper())
        restart_game = input("Want to play again? Type 'Y' to play again or 'N' to quit: ")
        if restart_game == "Y":
            continue
        elif restart_game == "N":
            break
    print(result)
