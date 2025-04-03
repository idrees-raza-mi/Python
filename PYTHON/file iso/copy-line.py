with open("this.txt", "r") as file:
    text = file.read()

with open("this_copy.txt", "w") as file:
    file.write(text)