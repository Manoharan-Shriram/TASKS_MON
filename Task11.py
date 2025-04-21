# 11. Write a python Function to count the number of vowels in a string. 

def vowcount(a):

    count=0
    b='aeiouAEIOU'
    for i in a:
        if i in b:
            count+=1
    print(f'The vowel count in the given string is {count}')



a=input("Enter the string: ")
vowcount(a)