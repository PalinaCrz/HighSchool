# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MiniWiki
class Colorizer:
    _codes = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "dim": "\033[2m",
        "underline": "\033[4m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "hidden": "\033[8m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
    }

    _env_var = "MINIWIKI_DISABLE_COLORS"

    @staticmethod
    def is_disabled():
        return os.environ.get(Colorizer._env_var, "").lower() in ("1", "true", "yes")

    @staticmethod
    def enable():
        if not Colorizer.is_disabled():
            os.environ[Colorizer._env_var] = "0"

    @staticmethod
    def disable():
        if Colorizer.is_disabled():
            os.environ.pop(Colorizer._env_var, None)

    @staticmethod
    def colorize(text, color):
        if Colorizer.is_disabled() or color not in Colorizer._codes:
            return text
        return Colorizer._codes[color] + text + Colorizer._codes["reset"]

    @staticmethod
    def tag(text, color):
        return Colorizer.colorize(f" [{text} ]", color)
