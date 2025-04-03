def game():
    return int(input("Enter your score: "))

score = game()

try:
    with open("Hi-score.txt", "r") as file:
        hi_score = int(file.read())
except FileNotFoundError:
    hi_score = 0

if score > hi_score:
    with open("Hi-score.txt", "w") as file:
        file.write(str(score))
    print("New Hi-score!")
else:
    print("Try again to beat the Hi-score.")