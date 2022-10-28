import numbers


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        elif isinstance(other, numbers.Real):
            return Fraction(self.a * other, self.b)
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        elif isinstance(other, numbers.Real):
            return Fraction(self.a * other, self.b)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction((self.a * other.b) + (other.a * self.b), self.b * other.b)
        elif isinstance(other, numbers.Real):
            return Fraction(self.a + other * self.b, self.b)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Fraction):
            return Fraction((self.a * other.b) + (other.a * self.b), self.b * other.b)
        elif isinstance(other, numbers.Real):
            return Fraction(self.a + other * self.b, self.b)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction((self.a * other.b) - (other.a * self.b), self.b * other.b)
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Fraction):
            return Fraction((self.a * other.b) - (other.a * self.b), self.b * other.b)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.a % other.a == 0 and self.b % other.b == 0) or (other.a % self.a == 0 and other.b % self.b == 0)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return (self.a * other.b > other.a * self.b)
        elif isinstance(other, numbers.Real):
            return (self.a > other * self.b)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (self.a * other.b < other.a * self.b)
        elif isinstance(other, numbers.Real):
            return (self.a < other * self.b)
        else:
            return NotImplemented

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return  self < other or self == other

    def __str__(self):
        return f"Fraction: {self.a}/{self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)  # Fraction: 21, 18
#f_c = f_a + 2
#print(f_c)
f_d = f_b * f_a
print(f_d)  # Fraction: 6, 18
#f_d = f_a * 2
#print(f_d)
f_e = f_a - f_b
print(f_e)  # Fraction: 3, 18

print(f_d <= f_c)  # True
print(f_d >= f_e)  # True
print(f_a == f_b)  # False