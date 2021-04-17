import colorama

from user_interaction import choose_word_to_guess, ask_for_letter, play_again
from print_game import print_game, print_win, print_lose


def full_game():

    colorama.init()

    games = 0
    wins = 0
    while True:

        word_to_guess = choose_word_to_guess()

        win = game(word_to_guess, games, wins)

        do_again = play_again()

        if not do_again:
            break

        games += 1
        wins += 1 if win==True else 0


def game(word_to_guess, games, wins):

    error = ""
    while True:

        print_game(word_to_guess, error=error, games=games, wins=wins)

        letter_guess = ask_for_letter()
        error = word_to_guess.check_letter_guess(letter_guess)

        if len(error)>0:
            continue

        word_to_guess.add_letter(letter_guess)

        if word_to_guess.guessed():
            print_win(word_to_guess, games=games, wins=wins)
            win = True
            break
        elif word_to_guess.lose():
            print_lose(word_to_guess, games=games, wins=wins)
            win = False
            break

    return win


if __name__ == "__main__":
    full_game()