# 7. Write a Python program to sum the first n prime numbers. User to input the n.

n=int(input("Enter the number: "))

sum=0

for i in range(n):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                sum+=i

print(sum)

    