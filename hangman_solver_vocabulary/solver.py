import numpy as np
from time import time

from nltk.corpus import words


word_guess = "super".upper()

LEN_WORD = len(word_guess)

word_list = np.asarray(words.words())

filter_length = np.vectorize(lambda word: len(word) == LEN_WORD)
upper_words = np.vectorize(lambda word: word.upper())

list_filtered = upper_words(word_list[filter_length(word_list)])

string_total = list("".join(list_filtered))

letters = [letter for letter, _ in sorted(zip(*np.unique(string_total, return_counts=True)), key=lambda x: -x[1])]

guessed_letters = []
fails = 0

print(letters)
for letter in letters:
    if letter in word_guess:
        last_guess_letter = letter
        last_guess_indexes = [index for index, l in enumerate(word_guess) if l==letter]
        break
    fails += 1

filter_letter = np.vectorize(lambda word: all([word[index]==last_guess_letter for index in last_guess_indexes]))

filter_words_letter = list_filtered[filter_letter(list_filtered)]

print(len(filter_words_letter))
print(filter_words_letter)
