import os
from store_draws import *
import numpy as np

from print_colors import PrintColors
from word_class import WordGuess


def _adjust_draw(draw: str, n_chars: int = 20) -> str:
    """
    Make all the line in a draw of the same length

    :param draw: the draw
    :param n_chars: the length each line should be
    :return: the adjusted draw
    """
    new_lines = []
    for line in draw.split("\n"):
        new_lines.append(line.ljust(n_chars))
    return "\n".join(new_lines)


def _change_color_draw(draw: str, color: str) -> str:
    """
    Change the color of a draw

    :param draw: the draw
    :param color: the color, supported colors are: "green", "yellow", "red"
    :return: the colored draw
    """
    new_lines = []
    for line in draw.split("\n"):
        try:
            new_lines.append(getattr(PrintColors, color)(line))
        except:
            raise ValueError(f"Color {color} not found.")
    return "\n".join(new_lines)


def _add_to_line(draw: str, string: str, line_add: int = 3) -> str:
    """
    Append a string to a certain line of the draw.

    :param draw: the draw
    :param string: the string to append
    :param line_add: the line where to append the string
    :return: the draw with the string
    """
    new_lines = []
    for index, line in enumerate(draw.split("\n")):
        if index == line_add:
            line += "\t\t" + string
        new_lines.append(line)
    return "\n".join(new_lines)


def _edit_draw(
    draw: str, before: str = "", after: str = "", before_line: str = ""
) -> str:
    """
    Edit a draw to render it better.

    :param draw: the draw to edit
    :param before: what to append before the draw
    :param after: what to append after the draw
    :param before_line: what to append at the beginning of each
        line of the draw
    :return: the edited draw
    """
    new_lines = [before]
    for line in draw.split("\n"):
        new_lines.append(before_line + line)
    new_lines.append(after)
    return "\n".join(new_lines)


steps = {
    0: _adjust_draw(step0),
    1: _adjust_draw(step1),
    2: _adjust_draw(step2),
    3: _adjust_draw(step3),
    4: _adjust_draw(step4),
    5: _adjust_draw(step5),
    6: _adjust_draw(step6),
    7: _adjust_draw(step7),
    8: _adjust_draw(step8),
}


def clean_screen():
    """
    Clean the terminal screen
    """
    os.system("cls" if os.name == "nt" else "printf '\033c'")


def print_game(
    word_to_guess: WordGuess,
    games: int,
    wins: int,
    tot_fails: int,
    error: str = "",
    before: str = "\n\n",
    after: str = "",
    before_line: str = "\t\t",
) -> None:
    """
    Print the game.

    :param word_to_guess: the word to guess, wrapped in its class
    :param games: the games played
    :param wins: the games won
    :param tot_fails: the sum of the fails in the games played
    :param error: error from the checks on the guessed letter
    :param before: what to append before the draw
    :param after: what to append after the draw
    :param before_line: what to append at the beginning of each
        line of the draw
    :return: None
    """

    # Clean the screen
    clean_screen()

    # Select the draw
    draw = steps[word_to_guess.fails]

    # Add some information to the draw
    draw = _add_to_line(draw, str(word_to_guess), line_add=3)
    draw = _add_to_line(
        draw,
        "Letters tried: " + word_to_guess.get_letters_tried(),
        line_add=6,
    )
    draw = _add_to_line(draw, PrintColors.red(error), line_add=8)
    if games > 0:
        draw = _add_to_line(
            draw,
            f"Wins: {wins}/{games}\tAverage fails:{np.round(tot_fails/games, 2)}",
            line_add=1,
        )

    # Edit the draw to render it better
    draw = _edit_draw(draw=draw, before=before, after=after, before_line=before_line)

    # Print the draw
    print(draw)


def print_win(
    word_to_guess: WordGuess, games: int, wins: int, tot_fails: int, before: str = "\n\n", after: str = "", before_line: str = "\t\t"
) -> None:
    """
    Print the win draw.

    :param word_to_guess: the word to guess, wrapped in its class
    :param games: the games played
    :param wins: the games won
    :param tot_fails: the sum of the fails in the games played
    :param error: error from the checks on the guessed letter
    :param before: what to append before the draw
    :param after: what to append after the draw
    :param before_line: what to append at the beginning of each
        line of the draw
    :return: None
    """

    # Clean the screen
    clean_screen()

    # Change the color of the draw to green
    draw = _change_color_draw(steps[word_to_guess.fails], "green")

    # Add some information to the draw
    draw = _add_to_line(draw, PrintColors.green(str(word_to_guess)), line_add=3)
    draw = _add_to_line(
        draw,
        "Letters tried: " + word_to_guess.get_letters_tried(),
        line_add=6,
    )
    if games > 0:
        draw = _add_to_line(
            draw,
            PrintColors.green(
                f"Wins: {wins+1}/{games+1}\tAverage fails:{np.round((tot_fails+word_to_guess.fails)/(games+1), 2)}"
            ),
            line_add=1,
        )

    # Edit the draw to render it better
    draw = _edit_draw(draw=draw, before=before, after=after, before_line=before_line)

    # Print the win screen
    print(draw)
    print(before_line + PrintColors.green("You Won!!!"))


def print_lose(word_to_guess: WordGuess, games: int, wins: int, tot_fails: int, before_line: str="\t\t") -> None:
    """
    Print the game over draw.

    :param word_to_guess: the word to guess, wrapped in its class
    :param games: the games played
    :param wins: the games won
    :param tot_fails: the sum of the fails in the games played
    :param before_line: what to append at the beginning of each
        line of the draw
    :return: None
    """

    # Clean the screen
    clean_screen()

    # Change the color of the draw to red
    draw = _change_color_draw(GAME_OVER, "red")

    # Add some information to the draw
    word = "".join(word_to_guess.word_to_guess)
    draw = _add_to_line(
        draw,
        PrintColors.red(f"The word was: {word}"),
        line_add=3,
    )
    if games > 0:
        draw = _add_to_line(
            draw,
            PrintColors.red(
                f"Wins: {wins}/{games+1}\tAverage fails:{np.round((tot_fails+word_to_guess.fails)/(games+1), 2)}"
            ),
            line_add=1,
        )

    # Edit the draw to render it better
    draw = _edit_draw(draw=draw, before_line=before_line)

    # Print the game over screen
    print(draw)
