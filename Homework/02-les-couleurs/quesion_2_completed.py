def color(color_name, font, intensity):
    color_map = {'red': 1, 'green': 2, "blue": 4, "yellow": 3, "purple": 5, "white": 0, "gray": 7}
    intensity_map = {"default": 3, "highlight": 4, "exaggerate": 9}
    font_map = {"bold": 1, "default": 0, "underline": 4, "revert": 7}

    def decorator(f):
        def inner(*arg, **kw):
            res = f"\033[{intensity_map[intensity]}{color_map[color_name]};{font_map[font]}m{f(*arg, **kw)}\033[0m"
            return res

        return inner

    return decorator


@color('red', 'revert', 'exaggerate')
def echo(s):
    return s


print(echo('hello'))
