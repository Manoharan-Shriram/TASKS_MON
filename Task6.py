# 6. Write a python Program to print the multiplication table (upto 10) of any number provided by the user

n=int(input("Enter the number: "))

for i  in range(1,11):
    print(f'{n} * {i} = {n*i}')