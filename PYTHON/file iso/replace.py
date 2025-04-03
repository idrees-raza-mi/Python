with open("file.txt", "r") as file:
    text = file.read()

text = text.replace("Donkey", "#####")

with open("file.txt", "w") as file:
    file.write(text)