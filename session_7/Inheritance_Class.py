import math

class Parallelogram:

    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def calculate_height(self):
        height = (math.sin(math.radians(self.alpha))) * self.b
        return height

    def calculate_perimeter(self):
        return (self.a + self.b) * 2

    def calculate_area(self):
        return self.calculate_height() * self.a

# Use of The Inheritance:
class Rectangle(Parallelogram):
    def __init__(self, a, b):

        super().__init__(a, b, 90)


p1 = Parallelogram(5, 10, 30)
print(p1.calculate_area())
print(p1.calculate_height())

p2 = Rectangle(5, 10)
print(p2.calculate_area())