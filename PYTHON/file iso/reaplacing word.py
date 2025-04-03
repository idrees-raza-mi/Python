words_to_censor = ["Donkey", "Dog", "Monkey"]  # Add more words as needed

with open("file.txt", "r") as file:
    text = file.read()

for word in words_to_censor:
    text = text.replace(word, "#####")

with open("file.txt", "w") as file:
    file.write(text)