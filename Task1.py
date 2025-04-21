# A list of words is given. Find the words from the list that have their second character in uppercase. ls = ['hello', 
# 'Dear', 'hOw', 'ARe', 'You'] 

l=['hello','Dear','hOw','ARe','You']

for i in l:
    if i[1].isupper():
        print(i)
