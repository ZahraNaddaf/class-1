class Tempreture:
    """
    example
    -------
    >>> t = Tempreture(27)
    >>> t.cels
    27.0
    >>> t.fahrenheit
    80.6
    >>> t.fahrenheit = 100
    >>> t.cels
    37.77777777777778

    """

    def __init__(self, celsius):
        self.cels = float(celsius)

    @property
    def fahrenheit(self):
        return (9 / 5) * self.cels + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.cels = (5 / 9) * (value - 32)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
