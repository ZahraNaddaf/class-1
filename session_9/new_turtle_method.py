import turtle


class NewTurtle(turtle.Turtle):

    def __init__(self, length, degree, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.length = length
        self.degree = degree
        self.speed(7)
        self.color((1, 0, 0))

    def turn(self):
        for i in range(4):
            self.forward(self.length)
            self.left(self.degree)


t = NewTurtle(200, 90)
t.turn()
