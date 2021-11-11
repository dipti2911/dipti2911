t1=(21)
t2=(23,)
print(t1)
#In tuple gives the comma even if it contain only single element
print(type(t1))
#output <class 'int'>
print(type(t2))
#output<class 'tuple'>


t3=(21,21,56,18,'bhupesh')
print(type(t3))
print(t3.count(21))
print(t3.index('bhupesh'))
print(t3*2)

#converting list to tuple

lst=[12,56,75,2,'mahi']
print(type(lst))
tpl1=tuple(lst)
[print(tpl1)]
print(type(tpl1))

#tuples are immutable if we want to change ,insert ,delete element in tuple it is not possible

t3[0]='dipu'
print(t3)

