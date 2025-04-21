# Write a Python function that accepts a string from user and calculates the number of upper-case letters and 
#  lower-case letters.

def charcount(S):
    uppercase_count=0
    lowercase_count=0
    for i in S:
        if i.isupper():
            uppercase_count+=1
        elif i.islower():
            lowercase_count+=1
    print(f'The number of Uppercase letters is {uppercase_count} and Lowercase letters is {lowercase_count}')

S=input("Enter the String: ")
charcount(S)



