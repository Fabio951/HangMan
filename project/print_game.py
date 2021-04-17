import os
from store_steps import *

from print_colors import PrintColors


def _adjust_draw(draw, n_chars=20):
    new_lines = []
    for line in draw.split("\n"):
        new_lines.append(line.ljust(n_chars))
    return "\n".join(new_lines)


def _change_color_draw(draw, color):
    new_lines = []
    for line in draw.split("\n"):
        try:
            new_lines.append(getattr(PrintColors, color)(line))
        except:
            raise ValueError(f"Color {color} not found.")
    return "\n".join(new_lines)


def _add_to_line(draw, string, line_add=3):
    new_lines = []
    for index, line in enumerate(draw.split("\n")):
        if index == line_add:
            line += "\t\t" + string
        new_lines.append(line)
    return "\n".join(new_lines)


def _edit_draw(draw, before="", after="", before_line=""):
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
    os.system("cls" if os.name == "nt" else "printf '\033c'")


def print_game(word_to_guess, games, wins, error="", before="\n\n", after="", before_line="\t\t"):
    clean_screen()

    draw = steps[word_to_guess.fails]

    draw = _add_to_line(draw, str(word_to_guess), line_add=3)
    draw = _add_to_line(
        draw,
        "Letters tried: " + word_to_guess.get_letters_tried(),
        line_add=6,
    )
    draw = _add_to_line(draw, PrintColors.red(error), line_add=8)
    if games>0:
        draw = _add_to_line(
            draw,
            f"Wins: {wins}/{games}",
            line_add=1,
        )

    draw = _edit_draw(draw=draw, before=before, after=after, before_line=before_line)

    print(draw)


def print_win(word_to_guess, games, wins, before="\n\n", after="", before_line="\t\t"):
    clean_screen()

    draw = _change_color_draw(steps[word_to_guess.fails], "green")
    draw = _add_to_line(draw, PrintColors.green(str(word_to_guess)), line_add=3)
    draw = _add_to_line(
        draw,
        "Letters tried: " + word_to_guess.get_letters_tried(),
        line_add=6,
    )
    if games>0:
        draw = _add_to_line(
            draw,
            PrintColors.green(f"Wins: {wins+1}/{games+1}"),
            line_add=1,
        )

    draw = _edit_draw(draw=draw, before=before, after=after, before_line=before_line)

    print(draw)
    print(before_line + PrintColors.green("You Won!!!"))


def print_lose(word_to_guess, games, wins, before_line="\t\t"):
    clean_screen()
    draw = _change_color_draw(GAME_OVER, "red")
    word = "".join(word_to_guess.word_to_guess)
    draw = _add_to_line(
        draw,
        PrintColors.red(f"The word was: {word}"),
        line_add=3,
    )
    if games>0:
        draw = _add_to_line(
            draw,
            PrintColors.red(f"Wins: {wins}/{games+1}"),
            line_add=1,
        )

    draw = _edit_draw(draw=draw, before_line=before_line)
    print(draw)
