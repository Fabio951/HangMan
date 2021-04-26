from print_game import clean_screen
from random_word import RandomWords

from print_colors import PrintColors
from word_class import WordGuess


def choose_word_to_guess() -> WordGuess:
    """
    Ask for the word to be guessed.

    :return: the word to guess, wrapped in a WordGuess class
    """

    # String to print when asking for the word
    ask_word = "Choose a word to be guessed. If left empty, a random word will be chosen for you.\n{error}\nInsert here: "

    error = ""
    while True:
        # Loop until a good word is passed

        # Clean the screen
        clean_screen()

        # Ask for the word
        word = input(ask_word.format(error=error))

        if (not word.isalpha() or not word.isascii()) and word != "":
            # If the word contains numbers or special characters, next time print an error
            error = PrintColors.red("You can only input a-z letters, no spaces")
        else:
            # If a good word is passed, break the loop
            break

    # If the user doesn't choose a word, a random word will be chosen instead
    if word == "":

        print("\nChoosing a random word ...")
        # Ask for a random word
        r = RandomWords()

        # Accept the random word if it does not contain special characters
        while True:
            word = r.get_random_word()
            if word is None:
                continue
            elif word.isalpha() and word.isascii():
                break

    # Wrap the word to guess in a WordGuess class
    word_to_guess = WordGuess(word)

    return word_to_guess


def ask_for_letter(before_line: str = "\t\t") -> str:
    """
    Ask for the letter guess

    :param before_line: what to append before the question
    :return: the letter guessed
    """
    letter_guess = input(before_line + "Guess the letter: ")
    return letter_guess


def play_again(before_line: str = "\t\t") -> bool:
    """
    Ask users if they want to play again

    :param before_line: what to append before the question
    :return: True if they want to play again, False otherwise
    """
    # Ask the question
    do_play_again = input("\n" + before_line + "Do you want to play again? (Y/N) ")

    # Positive answer is an answer that does not contain the letter "n".
    # An empty answer is considered a positive answer.
    do_play_again = not "n" in do_play_again.lower()

    return do_play_again
