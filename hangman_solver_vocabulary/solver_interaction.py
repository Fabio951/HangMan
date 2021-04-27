from copy import deepcopy as dcopy
import numpy as np
import os
from pyautogui import typewrite



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


def guess_letter(word, list_word):
    letters_index = [(letter, index) for index, letter in enumerate(word) if letter!="_"]

    filter_letter = np.vectorize(lambda word: all([word[index] == letter for letter, index in letters_index]))
    list_filtered = list_word[filter_letter(list_word)]

    if len(list_filtered)==0:
        return [], None

    f_set_words = np.vectorize(lambda word: "".join(set(word)))
    all_letters = list("".join(f_set_words(list_filtered)))
    letters_ordered = [letter for letter, _ in sorted(zip(*np.unique(all_letters, return_counts=True)), key=lambda x: -x[1]) if letter not in word]

    return letters_ordered[0], list_filtered if len(list_filtered)<=10 else None


clean_screen()
print("Loading vocabuary...")
vocabulary = load_vocabulary("american-english-insane")

while True:

    clean_screen()

    while True:
        try:
            n_letters = int(input("How many letters does the word have?(int)  "))
            break
        except:
            continue

    word = "_"*n_letters

    f_filter_length = np.vectorize(lambda word: len(word) == n_letters)
    list_filtered = vocabulary[f_filter_length(vocabulary)]

    letter_guessed = []
    while True:

        letter_guess, list_words = guess_letter(word, list_filtered)

        # Update word list with words without the letters guessed

        clean_screen()
        print("Letters tried: ", *letter_guessed)
        letter_guessed.append(letter)
        if list_words is not None:
            print("Possible words: ", *list_words)
        else:
            print("Possible words: Still too many")
        print(f"\nTry with the letter: {letter}")
        print("\nDid you get any improvement? If not, press Enter.\n")
        typewrite(word)
        word = input().upper()

        if len(letters_guess_ordered)==0:
            clean_screen()
            print("Sorry, I have no more suggestions for you :(")
            break
        elif "_" not in word:
            print("\nYay, we won! :D")
            break

    play_again = input("\nDo you want to play again? (y/n)  ")
    if "n" in play_again.lower():
        break
