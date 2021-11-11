n=int(input('Enter the number: '))
c=0
for a in range(1,n+1):
    if a%2!=0:
        print(a)
        c+=1
print('\n Total odd numbers are: ',c)
