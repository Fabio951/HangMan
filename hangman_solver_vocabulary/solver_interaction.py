import numpy as np
import os



def clean_screen():
    os.system("cls" if os.name == "nt" else "printf '\033c'")


def load_vocabulary(vocabulary):
    with open(f"dictionaries/{vocabulary}", "r") as f:
        vocabulary = np.asarray(f.read().split("\n"))

    f_check_format = np.vectorize(lambda word: word.isascii() and word.isalpha())
    f_upper_words = np.vectorize(lambda word: word.upper())

    vocabulary = np.asarray(list(vocabulary))
    vocabulary = f_upper_words(vocabulary[f_check_format(vocabulary)])
    vocabulary = np.asarray(list(set(vocabulary)))

    return vocabulary


vocabulary = load_vocabulary("american-english-insane")

while True:

    clean_screen()

    n_letters = input("How many letters does the word have?  ")

    f_filter_length = np.vectorize(lambda word: len(word) == n_letters)
    list_filtered = vocabulary[f_filter_length(vocabulary)]

    f_set_words = np.vectorize(lambda word: "".join(set(word)))
    while go_on:

        # type win to win

    play_again = input("Do you want to play again? (y/n)  ")
    if "n" in play_again.lower():
        break
