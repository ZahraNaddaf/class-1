class Tempreture:
    def __init__(self,celsius):
        self.cels = celsius

    @property
    def fahrenheit(self):
        return (9/5)*self.cels + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.cels = (5/9)*(value - 32)

t = Tempreture(27)
print(t.cels, t.fahrenheit)

t.fahrenheit = 100
print(t.cels, t.fahrenheit)
