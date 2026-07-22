# Write a program to print the multiplication table of a number using for loops in reversed order.

n = int(input("Enter the number for which you want the multiplication table: "))

for i in range(10, 0, -1):
    print(f"{n} * {i} = {n * i}")