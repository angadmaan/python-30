# Write a program to print the following star pattern.

#   *
#  * *
# * * * * * for n = 3

n = int(input("Enter your number: "))

for i in range(1, n + 1):
    if i == n:
        print("*" * (2 * n - 1))
    else:
        print(" " * (n - i) + "* " * i)
