# 15. Write a python function that copies a file reading and writing up to 50 characters at a time. 

with open('demo.txt','r') as f:
    line=f.read(50)

with open('demo2.txt','w') as f1:
    f1.write(line)
