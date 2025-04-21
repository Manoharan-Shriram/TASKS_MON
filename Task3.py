# Write a python program to search for a character and the count of its occurrence in a given string

k=input("Enter the character: ")
c="MANOHARAN"
count=0

if  k in c:
    print(c.count(k))
else:
    print("Not found")

