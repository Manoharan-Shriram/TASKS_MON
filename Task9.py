# . Write a python program to rotate a list by right n times with and without slicing technique

n=int(input("Enter the number of rotations: "))

l=[1,2,3,4,5,6,7,8,9]



for i in range(n):
    k=l.pop()
    l.insert(0,k) 
else:
    print(l)

# Slicing

n=int(input("Enter the number of rotations: "))

l=[1,2,3,4,5,6,7,8,9]



for i in range(n):
    k=l[-1]
    l.pop()
    l.insert(0,k) 
else:
    print(l)
