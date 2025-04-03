class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Language: {self.language}")

# Example usage
p1 = Programmer("Idrees", 30, "Python")
p2 = Programmer("Ahmed", 25, "JavaScript")
p1.display_info()
p2.display_info()
