class Rectangle():
    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio = (value/ self.area)** 0.5
        self.width *= ratio
        self.height *= ratio

    @property
    def perimeter(self):
        return (self.width + self.height) * 2

    @perimeter.setter
    def perimeter(self, value):
        ratio = value/self.perimeter


