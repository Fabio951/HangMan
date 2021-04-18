import colorama

from user_interaction import choose_word_to_guess, ask_for_letter, play_again
from print_game import print_game, print_win, print_lose


def full_game():

    colorama.init()

    games = 0
    wins = 0
    tot_fails = 0
    while True:

        word_to_guess = choose_word_to_guess()

        fails = game(word_to_guess, games, wins, tot_fails)

        do_again = play_again()

        if not do_again:
            break

        games += 1
        wins += 1 if fails<9 else 0
        tot_fails += fails


def game(word_to_guess, games, wins, tot_fails):

    error = ""
    while True:

        print_game(word_to_guess, error=error, games=games, wins=wins, tot_fails=tot_fails)

        letter_guess = ask_for_letter()
        error = word_to_guess.check_letter_guess(letter_guess)

        if len(error)>0:
            continue

        word_to_guess.add_letter(letter_guess)

        if word_to_guess.guessed():
            print_win(word_to_guess, games=games, wins=wins, tot_fails=tot_fails)
            break
        elif word_to_guess.lose():
            print_lose(word_to_guess, games=games, wins=wins, tot_fails=tot_fails)
            break

    return word_to_guess.fails


if __name__ == "__main__":
    full_game()