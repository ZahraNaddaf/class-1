class InvalidTypeValue(TypeError):
    pass


class InvalidSignValue(ValueError):
    pass


def fact(n):
    if not isinstance(n, int):
        raise InvalidTypeValue

    if n < 0:
        raise InvalidSignValue

    f = 1
    for i in range(n+1):
        f = i * f
    return f


print(fact(3))
