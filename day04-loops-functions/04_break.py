# Break Statement in Python

'break statement is used to come out of the loop when encountered. It instructs the program to - exit the loop now'

print("Example:")

for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break
print("\nloop exited")

print("\nAnother example:")

for i in range(0,80):
    if i==10:
        break
    print(i) # this will print 0,1,2,3,4,5,6,7,8,9
print("\nloop exited")
