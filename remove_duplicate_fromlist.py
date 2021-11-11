a=eval(input("enter the element of list"))
print(a)
b=[]
for each_value in a:
    if each_value not in b:
        b.append(each_value)
print(b)



l1=eval(input("enter the element of list"))
s1=set(l1)
print(s1)