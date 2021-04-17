class print_colors:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

    @staticmethod
    def purple(string):
        return f"{print_colors.PURPLE}{string}{print_colors.END}"

    @staticmethod
    def blue(string):
        return f"{print_colors.BLUE}{string}{print_colors.END}"

    @staticmethod
    def cyan(string):
        return f"{print_colors.CYAN}{string}{print_colors.END}"

    @staticmethod
    def green(string):
        return f"{print_colors.GREEN}{string}{print_colors.END}"

    @staticmethod
    def yellow(string):
        return f"{print_colors.YELLOW}{string}{print_colors.END}"

    @staticmethod
    def red(string):
        return f"{print_colors.RED}{string}{print_colors.END}"

    @staticmethod
    def bold(string):
        return f"{print_colors.BOLD}{string}{print_colors.END}"

    @staticmethod
    def underline(string):
        return f"{print_colors.UNDERLINE}{string}{print_colors.END}"
