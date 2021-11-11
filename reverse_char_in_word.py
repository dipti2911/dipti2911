s="dipti gokul patil"
temp=s.split()
print(temp)
result=[]
i=0
while i<len(temp):
    result.append(temp[i][::-1])
    i+=1
print(result)
output=' '.join(result)
print(output)

