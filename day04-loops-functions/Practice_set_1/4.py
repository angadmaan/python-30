# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter your number: "))

factorial = 1

if n < 0:
    print("Factorial of a negative number does not exist.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)
