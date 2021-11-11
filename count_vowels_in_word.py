s=input("Enter the string: ")
l=['a','e','i','o','u']
c=0
for a in s:
    for b in l:
        if a==b:
         c+=1
print(c)

#**********************************************

word=input("Enter the string: ")
vowels={'a','e','i','o','u'}
result={}
for c in word:
    if c in vowels:
        result[c]=result.get(c,0)+1
for k,v in result.items():
        print(k,"is present",v,"time")






