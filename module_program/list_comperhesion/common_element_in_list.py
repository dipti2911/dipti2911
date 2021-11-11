a=[2,3,4,6]
b=[2,4,6,9]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

c=[i for i in a if i in b]
