import re
s=input("Enter the string:-")
result=re.findall(r'i\w+',s)
print(result)
for a in result:
    if len(a)>5:
        print(a)






