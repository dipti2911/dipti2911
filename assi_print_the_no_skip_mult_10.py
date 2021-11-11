no=int(input("Enter the number"))
i=0
while i<no:
    i+=1
    if i%10==0:
        continue
    elif i>100:
        break
    else:
        print(i)

no=int(input("Enter the number"))
for no in range(1,no+1):
    if no%10==0:
        continue
    elif no>100:
        break
    else:
        print(no)



