import random

target_words = []
open_file = open("target_words.txt")
for line in open_file:
    words = line.split()
    target_words.append(words)

select_word = random.choice(target_words)
print(select_word)
