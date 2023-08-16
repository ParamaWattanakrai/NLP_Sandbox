def print_colored(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',
        'light_green': '\033[92m',  
        'light_blue': '\033[94m',
        'light_orange': '\033[38;2;255;165;0m'

    }
    print(colors.get(color.lower(), '') + text + colors['reset'])
