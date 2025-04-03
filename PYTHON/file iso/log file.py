with open("log.txt", "r") as file:
    text = file.read()

if "python" in text:
    print("The log file contains 'python'")
else:
    print("The log file does not contain 'python'")