from store_steps import *
from time import sleep
import sys
from colorama import Fore, Back
import os


colorama.init()


def change_color_draw(draw, color):


while True:




    do_continue, error = check_letter(letter_guess, word_to_guess)

    if do_continue:
        clean_screen()
        continue

    word_to_guess.add_letter(letter_guess)

    if word_to_guess.lives >= len(steps):
        break
