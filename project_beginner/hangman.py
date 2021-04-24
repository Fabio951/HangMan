import os

from store_draws import steps, GAME_OVER


def clean_screen():
    os.system("cls" if os.name == "nt" else "printf '\033c'")


clean_screen()

word = input("Choose a word: ").upper()

fails = 0
letters_tried = []
while fails < 9:
    clean_screen()

    print(steps[fails])
    print(
        "\n"
        + "".join([letter if letter in letters_tried else "_" for letter in word])
        + "\n"
    )

    letter_guess = input("\nGuess a letter: ").upper()
    if letter_guess not in word:
        fails += 1

    letters_tried.append(letter_guess)

    if all(letter in letters_tried for letter in word):
        break

clean_screen()
if fails == 9:
    print(GAME_OVER)
    print("\nThe word was " + word.upper())
    print("\nGame Over!")
else:
    print(steps[fails])
    print("\n" + word)
    print("\nYou Won!")
