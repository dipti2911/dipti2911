s="aabbxxynewoipp"
temp=[]
for a in s:
    if a not in temp:
        temp.append(a)
print(temp)
output=' '.join(temp)
print(output)