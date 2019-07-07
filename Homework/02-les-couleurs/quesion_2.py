def color_intensity(intensity):
    intensity_map = {"default": "3", "highlight": "4", "exaggerate": "9"}

    def decorator(f):
        def inner(*arg, **kw):
            out = f(*arg, **kw)
            return "\033[" + intensity_map[intensity] + "1;0m" + out + "\033[0m"

        return inner

    return decorator


def color(color_name):
    color_map = {'red': "31", 'green': "32", "blue": "34", "yellow": "33", "purple": '35', "white": "30", "gray": "37"}

    def decorator(f):
        def inner(*arg, **kw):
            out = f(*arg, **kw)
            return "\033[" + color_map[color_name] + ";0m" + out + "\033[0m"

        return inner

    return decorator


def font_style(font):
    font_map = {"bold": "1m", "default": "0m", "underline": "4m", "revert": "7m"}

    def decorator(f):
        def inner(*arg, **kw):
            out = f(*arg, **kw)
            return "\033[31;" + font_map[font] + out + "\033[0m"

        return inner

    return decorator


@color_intensity("exaggerate")
@font_style("revert")
@color("green")
def echo(s):
    return s


print(echo("hello"))