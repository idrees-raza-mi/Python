with open("log.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    if "python" in line:
        print(f"'python' found at line {i}")