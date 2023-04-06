import random

result = [" "] * 5
target_words = []
open_file = open("target_words.txt", "r")

# Open file and get target word.
word_to_find = random.choice(open_file.read().splitlines())
print(word_to_find)

while True:
    user_word = input("Enter a 5 letter word: ")
    if len(user_word) < 5 or len(user_word) > 5:
        print("please enter a 5 letter word")
        continue
    for position in range(len(word_to_find)):
        if user_word[position] == word_to_find[position]:
            result[position] = word_to_find[position]
        # need to fix bug here involving user word with more identical letters than target word.
        elif user_word[position] in word_to_find:
            if user_word[position] is not word_to_find[position]:
                result[position] = "-"
    if word_to_find == user_word:
        print("Nice! you guessed the word. It was:", word_to_find)
        break
    print(result)
