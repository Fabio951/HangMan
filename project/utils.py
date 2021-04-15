from store_steps import *
from time import sleep
import sys
import os


def edit_draw(draw, before="", after="", before_line=""):
    lines = [before]
    for line in draw.split("\n"):
        line = before_line + line
        lines.append(line)
    lines.append(after)
    return "\n".join(lines)


def clean_screen():
    os.system("cls" if os.name == "nt" else "printf '\033c'")


class print_colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    @staticmethod
    def purple(string):
        return f"{print_colors.PURPLE}{string}{print_colors.END}"

    @staticmethod
    def blue(string):
        return f"{print_colors.BLUE}{string}{print_colors.END}"

    @staticmethod
    def cyan(string):
        return f"{print_colors.CYAN}{string}{print_colors.END}"

    @staticmethod
    def green(string):
        return f"{print_colors.GREEN}{string}{print_colors.END}"

    @staticmethod
    def yellow(string):
        return f"{print_colors.YELLOW}{string}{print_colors.END}"

    @staticmethod
    def red(string):
        return f"{print_colors.RED}{string}{print_colors.END}"

    @staticmethod
    def bold(string):
        return f"{print_colors.BOLD}{string}{print_colors.END}"

    @staticmethod
    def underline(string):
        return f"{print_colors.UNDERLINE}{string}{print_colors.END}"


class WordGuess:

    def __init__(self, word_to_guess):
        self.word_to_guess = list(word_to_guess.upper())
        self.letters_tried = []
        self.last_letter = ""

    def add_letter(self, letter):
        self.letters_tried.append(letter.upper())
        self.last_letter = letter.upper()

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

word = WordGuess('ciao')

print(word)

word.add_letter('i')

print(word)

word.add_letter('F')

print(word)

word.add_letter('a')

print(word)
word.add_letter('c')
print(word)
word.add_letter('h')
print(word)
word.add_letter('o')

print(word)


a=b

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

word_to_guess = "Minion"

clean_screen()

for step, draw in steps.items():

    draw_to_print = edit_draw(draw=draw, before=before, after=after, before_line=before_line)
    draw_with_word = add_word_to_print(draw_to_print, word)
    print(draw_to_print)
    a = input(before_line + "Guess the letter: ")

    clean_screen()
