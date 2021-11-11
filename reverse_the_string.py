s=input("enter the string: ")
print(s[::-1])

print("\n Second way to reverse the string")
s=input("Enter the string: ")
i=len(s)-1
result=''
while i>=0:
    result=result+s[i]
    i=i-1
print(result)
