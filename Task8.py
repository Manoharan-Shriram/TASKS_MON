# 8. Write a python program to find a maximum and minimum number in a list without using an inbuilt function


l=[9,4,8,7,1,3,5]

max=0
min=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

for i in l:
    if i>max:
        max=i
    
    if i<min:
        min=i

print(f'max value:{max}')
print(f'min value: {min}')