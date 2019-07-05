class Parallelogram:

    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def area(self):
        import math
        return (math.sin(math.radians(self.alpha)))*self.b*self.a

p1 = Parallelogram(5,10,30)
print(p1.area())