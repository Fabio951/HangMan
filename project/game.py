import colorama

from user_interaction import choose_word_to_guess, ask_for_letter, play_again
from print_game import print_game, print_win, print_lose
from word_class import WordGuess


def full_game():
    """
    Start the game and have fun!
    """

    # Initialize the colorama library. It is needed since Windows needs a different
    # setup from MacOS and Linux.
    colorama.init()

    games = 0
    wins = 0
    tot_fails = 0
    while True:
        # Cycle through the games

        # Initialize the word to guess
        word_to_guess = choose_word_to_guess()

        # Run the single game
        fails = game(word_to_guess, games, wins, tot_fails)

        # Ask if want to play again
        do_again = play_again()

        # Break if user don't want to play again
        if not do_again:
            break

        # Update stats
        games += 1
        wins += 1 if fails < 9 else 0
        tot_fails += fails


def game(word_to_guess: WordGuess, games: int, wins: int, tot_fails: int) -> int:
    """
    Run the single game.

    :param word_to_guess: the word to guess, wrapped in a class
    :param games: number of games played
    :param wins: number of games won
    :param tot_fails: number of total fails in previous games
    :return: number of fails in this run
    """

    error = ""
    while True:
        # Cycle through letter guess

        # Print the game display
        print_game(
            word_to_guess, error=error, games=games, wins=wins, tot_fails=tot_fails
        )

        # Ask for a letter
        letter_guess = ask_for_letter()
        # Make some checks on the letter guessed
        error = word_to_guess.check_letter_guess(letter_guess)

        # If an error is found in the letter guessed, we ask the user to try another letter
        if len(error) > 0:
            continue

        # We store the letter guessed
        word_to_guess.add_letter(letter_guess)

        # If the word is guessed or you finish the lives, the game ends
        if word_to_guess.guessed():
            print_win(word_to_guess, games=games, wins=wins, tot_fails=tot_fails)
            break
        elif word_to_guess.lose():
            print_lose(word_to_guess, games=games, wins=wins, tot_fails=tot_fails)
            break

    return word_to_guess.fails


if __name__ == "__main__":
    full_game()
