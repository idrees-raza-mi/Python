# calulate the factorial of the given number number using while loop\
n = int(input("Insert a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
    print(f"The factorial of {n} is {fact}")
