from colorama import Fore


class PrintColors:
    @staticmethod
    def red(string):
        # Print the string in a red color
        return Fore.RED + string + Fore.RESET

    @staticmethod
    def green(string):
        # Print the string in a green color
        return Fore.GREEN + string + Fore.RESET

    @staticmethod
    def yellow(string):
        # Print the string in a yellow color
        return Fore.YELLOW + string + Fore.RESET
