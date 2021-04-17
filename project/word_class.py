from print_colors import PrintColors


class WordGuess:
    def __init__(self, word_to_guess):
        self.word_to_guess = list(word_to_guess.upper())
        self.letters_tried = []
        self.last_letter = ""
        self.fails = 0

    def check_letter_guess(self, letter):
        if len(letter) > 1:
            return "You can only type one letter per time"
        elif len(letter) == 0:
            return "You need to type a letter"
        elif not letter.isalpha():
            return "You can only type letters a-z"
        elif letter.upper() in self.letters_tried:
            return "You already tried this letter"
        else:
            return ""

    def add_letter(self, letter):

        letter = letter.upper()

        if letter not in self.word_to_guess:
            self.fails += 1

        self.letters_tried.append(letter)
        self.last_letter = letter

    def __repr__(self):

        if self.guessed():
            return PrintColors.green("".join(self.word_to_guess))
        else:
            string_to_print = ""
            for letter in self.word_to_guess:
                if letter in self.letters_tried:
                    letter = (
                        PrintColors.green(letter)
                        if letter == self.last_letter
                        else letter
                    )
                    string_to_print += letter
                else:
                    string_to_print += "_"

        if self.last_letter not in self.word_to_guess and len(self.letters_tried) > 0:
            string_to_print = PrintColors.red(string_to_print)

        return string_to_print

    def get_letters_tried(self):
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

    def guessed(self):
        return set(self.word_to_guess).issubset(set(self.letters_tried))

    def lose(self):
        return self.fails >= 9
