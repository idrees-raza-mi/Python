n = 3 # Size of the pattern
for i in range(n):
    print("*", end=" ")
print()
for i in range(n - 3):
    print(" ", end=" ")
print("*", end=" ")
print(" " * (n - 2), "*")
for i in range(n):
    print("*", end=" ")
print()

