from store_steps import *
from time import sleep
import sys
import colorama
from colorama import Fore, Back
import os
from random_word import RandomWords


colorama.init()
r = RandomWords()


def adjust_draw(draw, n_chars=20):
    new_lines = []
    for line in draw.split("\n"):
        new_lines.append(line.ljust(n_chars))
    return "\n".join(new_lines)


def edit_draw(draw, before="", after="", before_line=""):
    new_lines = [before]
    for line in draw.split("\n"):
        new_lines.append(before_line + line)
    new_lines.append(after)
    return "\n".join(new_lines)


def add_to_line(draw, string, line_word=3):
    new_lines = []
    for index, line in enumerate(draw.split("\n")):
        if index == line_word:
            line += "\t\t" + string
        new_lines.append(line)
    return "\n".join(new_lines)


def check_letter(letter_guess, word_to_guess):

    if len(letter_guess) > 1:
        return True, "You can only type one letter per time"
    elif len(letter_guess) == 0:
        return True, "You need to type a letter"
    elif not letter_guess.isalpha():
        return True, "You can only type letters a-z"
    elif letter_guess.upper() in word_to_guess.letters_tried:
        return True, "You already tried this letter"
    else:
        return False, ""


def change_color_draw(draw, color):
    new_lines = []
    for line in draw.split("\n"):
        try:
            new_lines.append(getattr(print_colors, color)(line))
        except:
            raise ValueError(f"Color {color} not found.")
    return "\n".join(new_lines)


def clean_screen():
    os.system("cls" if os.name == "nt" else "printf '\033c'")


class print_colors:
    @staticmethod
    def red(string):
        return Fore.RED + string + Fore.RESET

    @staticmethod
    def green(string):
        return Fore.GREEN + string + Fore.RESET

    @staticmethod
    def yellow(string):
        return Fore.RED + string + Fore.RESET


class WordGuess:
    def __init__(self, word_to_guess):
        self.word_to_guess = list(word_to_guess.upper())
        self.letters_tried = []
        self.last_letter = ""
        self.lives = 0

    def add_letter(self, letter):

        letter = letter.upper()

        if letter not in self.word_to_guess:
            self.lives += 1

        self.letters_tried.append(letter)
        self.last_letter = letter

    def __repr__(self):

        if self.guessed():
            return print_colors.green("".join(self.word_to_guess))

        string_to_print = ""
        for letter in self.word_to_guess:
            if letter in self.letters_tried:
                letter = (
                    print_colors.green(letter) if letter == self.last_letter else letter
                )
                string_to_print += letter
            else:
                string_to_print += "_"

        if self.last_letter not in self.word_to_guess and len(self.letters_tried) > 0:
            string_to_print = print_colors.red(string_to_print)

        return string_to_print

    def get_string_letters(self):
        letters_to_print = []
        for letter in self.letters_tried:
            if letter in self.word_to_guess:
                letters_to_print.append(print_colors.green(letter))
            else:
                letters_to_print.append(print_colors.red(letter))

        return ", ".join(letters_to_print)

    def guessed(self):
        return set(self.word_to_guess).issubset(set(self.letters_tried))


steps = {
    0: adjust_draw(step0),
    1: adjust_draw(step1),
    2: adjust_draw(step2),
    3: adjust_draw(step3),
    4: adjust_draw(step4),
    5: adjust_draw(step5),
    6: adjust_draw(step6),
    7: adjust_draw(step7),
    8: adjust_draw(step8),
}

before = "\n\n"
after = ""
before_line = "\t\t"

clean_screen()
word = input(
    "Choose a word to be guessed. If left empty, a random word will be chosen for you.\n\n"
)
if word == "":
    print("\nChoosing a random word ...")
    while True:
        word = r.get_random_word()
        if word.isalpha():
            break

word_to_guess = WordGuess(word)

clean_screen()

error = ""
while True:

    draw_lives = steps[word_to_guess.lives]
    draw_with_word = add_to_line(draw_lives, str(word_to_guess), line_word=3)
    draw_with_word = add_to_line(
        draw_with_word,
        "Letters tried: " + word_to_guess.get_string_letters(),
        line_word=6,
    )
    draw_with_word = add_to_line(draw_with_word, print_colors.red(error), line_word=8)
    draw_to_print = edit_draw(
        draw=draw_with_word, before=before, after=after, before_line=before_line
    )
    print(draw_to_print)

    letter_guess = input(before_line + "Guess the letter: ")

    do_continue, error = check_letter(letter_guess, word_to_guess)

    if do_continue:
        clean_screen()
        continue

    word_to_guess.add_letter(letter_guess)

    if word_to_guess.lives >= len(steps):
        clean_screen()
        draw_game_over = change_color_draw(GAME_OVER, "red")
        draw_game_over = add_to_line(
            draw_game_over,
            print_colors.red(f"The word was: {word.upper()}"),
            line_word=3,
        )
        print(
            edit_draw(
                draw=draw_game_over, before="", after=after, before_line=before_line
            )
        )
        break
    elif word_to_guess.guessed():
        clean_screen()

        draw_lives = change_color_draw(steps[word_to_guess.lives], "green")
        draw_with_word = add_to_line(
            draw_lives, print_colors.green(str(word_to_guess)), line_word=3
        )
        draw_with_word = add_to_line(
            draw_with_word,
            "Letters tried: " + word_to_guess.get_string_letters(),
            line_word=6,
        )
        draw_to_print = edit_draw(
            draw=draw_with_word, before=before, after=after, before_line=before_line
        )
        print(draw_to_print)
        print(before_line + print_colors.green("You Won!!!"))
        break
    else:
        clean_screen()
