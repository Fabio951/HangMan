from colorama import Fore


class PrintColors:
    @staticmethod
    def red(string):
        return Fore.RED + string + Fore.RESET

    @staticmethod
    def green(string):
        return Fore.GREEN + string + Fore.RESET

    @staticmethod
    def yellow(string):
        return Fore.YELLOW + string + Fore.RESET
