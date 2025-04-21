# 14. Write functions called is _sorted that takes a list as a parameter and returns True if the list is sorted in 
# ascending order and False otherwise and has_ duplicates that takes a list and returns True if there is any 
# element that appears more than once. It should not modify the original list. 

def _sorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    else:
        return  True
    

def _hasduplicates(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                return True
    else:
        
        return False



#True
l1=[1,2,3,4,5,6,7,8,9]
k=_sorted(l1)
print(k) 

#False
l2=[1,2,3,4,5,6,11,7,8,9]
k=_sorted(l2)
print(k) 

# True
l3=[1,1,2,3,4,5]
p=_hasduplicates(l3)
print(p)

#False
l4=[1,2,3,4,5]
p=_hasduplicates(l4)
print(p)



