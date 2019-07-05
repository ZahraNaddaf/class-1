import math

class Parallelogram:

    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def calculate_height(self):
        theta = (math.radians(self.alpha))
        return math.sin(theta)*self.b

    def calculate_perimeter(self):
        return (self.a + self.b) * 2

    def calculate_area(self):
        return self.calculate_height() * self.a


p1 = Parallelogram(5, 10, 30)
print(p1.calculate_area())
print(p1.calculate_height())



# the first test
#class Parallelogram:

#   def __init__(self, a, b, alpha):
#      self.a = a
#      self.b = b
#      self.alpha = alpha

# def area(self):
#       import math
#       return (math.sin(math.radians(self.alpha))) * self.b * self.a
