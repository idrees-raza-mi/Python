with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    text1 = file1.read()
    text2 = file2.read()

if text1 == text2:
    print("The files are identical")
else:
    print("The files are not identical")