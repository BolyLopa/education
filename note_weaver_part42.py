# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: NoteWeaver
import os, sys

def enable_ansi():
    if sys.platform == 'win32':
        try:
            os.system('')
        except:
            pass

class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'
    FG_BRIGHT_BLACK = '\033[90m'
    FG_BRIGHT_RED = '\033[91m'
    FG_BRIGHT_GREEN = '\033[92m'
    FG_BRIGHT_YELLOW = '\033[93m'
    FG_BRIGHT_BLUE = '\033[94m'
    FG_BRIGHT_MAGENTA = '\033[95m'
    FG_BRIGHT_CYAN = '\033[96m'
    FG_BRIGHT_WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def colorize(text, fg, bg=None):
    if bg:
        return f'{fg}{bg}{text}{Color.RESET}'
    return f'{fg}{text}{Color.RESET}'

def success(text):
    return colorize(text, Color.FG_GREEN, Color.BG_GREEN)

def error_text(text):
    return colorize(text, Color.FG_RED, Color.BG_RED)

def warning_text(text):
    return colorize(text, Color.FG_YELLOW, Color.BG_YELLOW)

def info_text(text):
    return colorize(text, Color.FG_CYAN, Color.BG_CYAN)

def dim(text):
    return colorize(text, Color.DIM)

def bold(text):
    return colorize(text, Color.BOLD)

def reverse(text):
    return colorize(text, Color.REVERSE)

def blink(text):
    return colorize(text, Color.BLINK)
