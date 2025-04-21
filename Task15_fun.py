# 15. Write a python function that copies a file reading and writing up to 50 characters at a time. 
def paste(w):
    with open('demo2.txt','w') as f1:
        f1.write(w)


with open('demo.txt','r') as f:
        w=f.read(50)

paste(w)