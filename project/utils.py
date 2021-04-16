from store_steps import *
from time import sleep
import sys
from colorama import Fore, Back, init
import os


init()

def edit_draw(draw, before="", after="", before_line=""):
    new_lines = [before]
    for line in draw.split("\n"):
        line = before_line + line
        new_lines.append(line.ljust(20))
    new_lines.append(after)
    return "\n".join(new_lines)


def add_word_to_print(draw, word):
    new_lines = []
    for index, line in enumerate(draw.split("\n")):
        if index==3:
            line += '\t\t' + str(word)
        new_lines.append(line)
    return "\n".join(new_lines)


def clean_screen():
    os.system("cls" if os.name == "nt" else "printf '\033c'")


class print_colors:

    @staticmethod
    def red(string):
        return Fore.RED + string + Fore.RESET

    @staticmethod
    def green(string):
        return Fore.CYAN + string + Fore.RESET

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
        string_to_print = ""
        for letter in self.word_to_guess:
            if letter in self.letters_tried:
                letter = print_colors.green(letter) if letter==self.last_letter else letter
                string_to_print += letter
            else:
                string_to_print += '_'

        if self.last_letter not in self.word_to_guess and len(self.letters_tried)>0:
            string_to_print = print_colors.red(string_to_print)

        return string_to_print


steps = {
    0: step0,
    1: step1,
    2: step2,
    3: step3,
    4: step4,
    5: step5,
    6: step6,
    7: step7,
    8: step8,
    9: step9,
}

before = ""
after = ""
before_line = ""

word = "Minion"

word_to_guess = WordGuess(word)

clean_screen()

while True:

    draw_lives = steps[word_to_guess.lives]
    draw_to_print = edit_draw(draw=draw_lives, before=before, after=after, before_line=before_line)
    draw_with_word = add_word_to_print(draw_to_print, word_to_guess)
    print(draw_with_word)

    letter_guess = input(before_line + "Guess the letter: ")

    word_to_guess.add_letter(letter_guess)

    if word_to_guess.lives >= len(steps):
        print(print_colors.red('GAME OVER'))

    clean_screen()
