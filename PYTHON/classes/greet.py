import math

class Calculator:
    def square(self, number):
        return number ** 2

    def cube(self, number):
        return number ** 3

    def square_root(self, number):
        return math.sqrt(number)

    @staticmethod
    def greet():
        print("Hello, User!")

# Example usage
calc = Calculator()
calc.greet()