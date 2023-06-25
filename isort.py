def isort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 & key<l[j]:
            l[j+1]=l[j]
            j-=l
        l[j+1]=key
            
l=[20,54,63,58,47]
isort(l)
print("sorted list is")
for i in range (len(l)):
    print("l[i]",end="")
    