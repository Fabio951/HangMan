from print_colors import PrintColors


class WordGuess:
    """
    A class to handle easier the word to be guessed
    """

    def __init__(self, word_to_guess: str):
        """
        Initialize the class with the word to be guessed
        """
        # We transform all the user inputs in capital letters
        self.word_to_guess = list(word_to_guess.upper())
        self.letters_tried = []
        self.last_letter = ""
        self.fails = 0


    def check_letter_guess(self, letter: str) -> str:
        """
        Makes some checks on the letter guessed

        :param letter: the letter guessed
        :return: the error
        """

        if len(letter) > 1:
            # Check if the user typed more than one letter
            return "You can only type one letter per time"

        elif len(letter) == 0:
            # Check if the user typed nothing
            return "You need to type a letter"

        elif not letter.isalpha():
            # Check if the user typed a number or a special character
            return "You can only type letters a-z"

        elif letter.upper() in self.letters_tried:
            # Check if the user already tried this letter
            return "You already tried this letter"

        else:
            # Everything ok
            return ""


    def add_letter(self, letter: str) -> None:
        """
        Store the letter guessed
        """

        # Transform the letter to a capital letter
        letter = letter.upper()

        if letter not in self.word_to_guess:
            # Letter not in the word to guess
            self.fails += 1

        # Store the letter
        self.letters_tried.append(letter)
        self.last_letter = letter


    def __repr__(self):
        """
        The __repr__ function tells the class what to output if the
        functions str() and print() are called on the class.
        """

        if self.guessed():
            # If the word has been guessed, we represent the full word
            # with a green color.
            return PrintColors.green("".join(self.word_to_guess))

        else:
            string_to_print = ""
            for letter in self.word_to_guess:

                if letter in self.letters_tried:
                    # The letter has already been guessed.
                    # We print it in green if it was the last letter guessed,
                    # otherwise we use the default terminal color.
                    letter = (
                        PrintColors.green(letter)
                        if letter == self.last_letter
                        else letter
                    )
                    string_to_print += letter

                else:
                    # The letter has not been guessed yet.
                    # We represent it with an underscore.
                    string_to_print += "_"

        if self.last_letter not in self.word_to_guess and len(self.letters_tried) > 0:
            # If the previous guessed letter was not in the word to guess,
            # we change the color of the word to red.
            string_to_print = PrintColors.red(string_to_print)

        return string_to_print


    def get_letters_tried(self) -> str:
        """
        Get a string with the letters tried.
        """
        # If the letter is present in the word to guess, it will
        # be represented in green, otherwise in red.
        letters_to_print = [
            PrintColors.green(letter)
            if letter in self.word_to_guess
            else PrintColors.red(letter)
            for letter in self.letters_tried
        ]
        # letters_to_print = []
        # for letter in self.letters_tried:
        #     if letter in self.word_to_guess:
        #         letters_to_print.append(print_colors.green(letter))
        #     else:
        #         letters_to_print.append(print_colors.red(letter))
        return ", ".join(letters_to_print)


    def guessed(self) -> bool:
        """
        Return True if the word has been guessed
        """
        return set(self.word_to_guess).issubset(set(self.letters_tried))


    def lose(self) -> bool:
        """
        Return True if the user lost all of their lives
        """
        return self.fails >= 9
