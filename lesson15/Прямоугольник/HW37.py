import numbers


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width, (self.get_square() + other.get_square())/self.width)
        if isinstance(other, numbers.Real):
            return Rectangle(self.width, (self.get_square() + other) / self.width)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width, (self.get_square() + other.get_square())/self.width)
        if isinstance(other, numbers.Real):
            return Rectangle(self.width, (self.get_square() + other) / self.width)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, numbers.Real):
            return Rectangle(self.width, (self.get_square() * n)/self.width)
        else:
            return NotImplemented

    def __str__(self):
        return f"rectangle [width = {self.width}, height = {self.height}]"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square())  # 8
print(r2.get_square())  # 18
print(r1 == r2)

r3 = r1 + 2
print(r3.get_square())  # 26

r4 = r1 * 4
print(r4.get_square())  # 32