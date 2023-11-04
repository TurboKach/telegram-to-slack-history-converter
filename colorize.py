class Colorize:
    """
    Example usage:
    Colorize.print('Hello, World!', Colorize.FG.red, Colorize.BG.black)
    """

    class FG:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class BG:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
        darkgrey = '\033[100m'
        lightred = '\033[101m'
        lightgreen = '\033[102m'
        yellow = '\033[103m'
        lightblue = '\033[104m'
        pink = '\033[105m'
        lightcyan = '\033[106m'

    reset = '\033[0m'

    @classmethod
    def color_text(cls, text: str = '', text_color: str = '', background_color: str = '') -> str:
        """
        Returns a string with colored text.
        :param text:
        :param text_color: one of Colorize.FG
        :param background_color: one of Colorize.BG
        :return:
        """
        text_color_code = text_color if text_color else ''
        background_color_code = background_color if background_color else ''
        return f"{text_color_code}{background_color_code}{text}{cls.reset}"

    @classmethod
    def print(cls, text: str = '', text_color: str = '', background_color: str = ''):
        """
        Prints colored text.
        :param text:
        :param text_color: one of Colorize.FG
        :param background_color: one of Colorize.BG
        :return:
        """
        print(cls.color_text(text, text_color, background_color))


if __name__ == '__main__':
    Colorize.print(
        text='Welcome to Telegram to Slack chat history converter\n',
        text_color=Colorize.FG.red,
        # No need to set background_color if you want it to be default
    )
