# Write a program to accept 2 numbers from users and display the sum of odd numbers and even numbers that 
# fall between them (ex 12 and 37)

n1=int(input("Enter the number1:"))
n2=int(input("Enter the number2:"))

odd_num_sum=0
even_num_sum=0

for i in range(n1,n2+1):
    if i%2==0:
        even_num_sum+=i
    elif i%2==1:
        odd_num_sum+=i

print(f'The odd numbers sum is {odd_num_sum}')
print(f'The even numbers sum is {even_num_sum}')
