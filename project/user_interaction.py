from print_game import clean_screen
from random_word import RandomWords

from print_colors import PrintColors
from word_class import WordGuess


def choose_word_to_guess():

    ask_word = "Choose a word to be guessed. If left empty, a random word will be chosen for you.\n{error}\nInsert here: "

    error = ""
    while True:

        clean_screen()

        word = input(ask_word.format(error=error))

        if not word.isalpha() and word != "":
            error = PrintColors.red("You can only input a-z letters, no spaces")
        else:
            break

    if word == "":
        print("\nChoosing a random word ...")
        r = RandomWords()
        while True:
            word = r.get_random_word()
            if word is None:
                continue
            elif word.isalpha():
                break

    word_to_guess = WordGuess(word)

    return word_to_guess


def ask_for_letter(before_line="\t\t"):
    letter_guess = input(before_line + "Guess the letter: ")
    return letter_guess

def play_again(before_line="\t\t"):
    do_play_again = input("\n" + before_line + "Do you want to play again? (Y/N) ")
    do_play_again = not 'n' in do_play_again.lower()
    return do_play_again