# 13. Python program to display the given integer in reverse order using the function without an in- built function.


n=int(input("Enter the number: "))

temp=n

rev=0

while temp > 0:
    
    k=temp%10
    rev=rev*10+k
   
    temp//=10

print(rev)
