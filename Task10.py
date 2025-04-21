# Write a python Function to generate n random numbers and list the even and odd numbers in that list. User to 
# input the n

import random
def oddeven(n):
    EL=[]
    OL=[]

    for i in range(n):
        m=random.randint(1,n)
        if m%2==0:
            EL.append(m)
        else:
            OL.append(m)

    print(f'The Even number list is {EL}  and odd number list is {OL}')

n=int(input())
oddeven(n)
