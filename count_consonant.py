str=input("enter the string: ")
#vowels={'a','e','i','o','u'}
c=0
#for a in str:
for b in str:
    if not b in('a','e','i','o','u',' '):
        c+=1
print(c)

