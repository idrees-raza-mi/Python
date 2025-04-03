import math

class Calculator:
    def square(self, number):
        return number ** 2

    def cube(self, number):
        return number ** 3

    def square_root(self, number):
        return math.sqrt(number)

# Example usage
calc = Calculator()
print(calc.square(4))
print(calc.cube(3))
print(calc.square_root(16))