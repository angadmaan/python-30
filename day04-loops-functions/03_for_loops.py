# For Loop

# A for loop is used iterate through a sequence like list, tuple, or string.

print("Syntax:")

# for (item) in (sequence):  
    # block of code

# Note: 'item' is just a variable, you can use any name in its place.

l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8


# Range Function:

print("range() function generates a sequence of numbers:")

for i in range(5):  # generates numbers from 0 to 4
    print(i)        # 0 1 2 3 4

print("range(start, stop, step):")

for i in range(2, 10, 2):  # generates even numbers from 2 to 8; here 2 is step
    print(i)                # 2 4 6 8

print("for loop with else:")

for i in range(5):
    print(i)
else:
    print("Done!")



