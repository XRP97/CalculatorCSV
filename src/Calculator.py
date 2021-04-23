from addition import addition
from subtraction import subtraction
from division import division
from multiplication import multiplication
from squareRoot import square_root
from square import square


class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

# Square Root on Calculator Test keep failing
    def square_root(self, a):
        self.result = square_root(a)
        return self.result


# To validate class script

# calc = Calculator()
# print(calc.add(1, 2))
