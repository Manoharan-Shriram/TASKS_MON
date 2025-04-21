# Try above problem using regex to create random string and check if your function works correctly.

import re
import random

def regfun(a):
    pattern='[aeiouAEIOU]'
    m=re.findall(pattern,a)
    print(m)
    print(len(m))



s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
q=random.sample(s,k=10)
a=''
for i in q:
    a+=i
print(a)
regfun(a)

