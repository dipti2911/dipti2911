i=[int(i) for i in input("Enter the numbers:=-").split()]
l=[]
for each_value in i:
    if not each_value in l:
        l.append(each_value)
print(l)



