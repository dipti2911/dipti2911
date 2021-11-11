list=[int(y) for y in input("Enter the numbers: ").split()]
for a in list:
    if a%2==0:
        print(a)
print(list)


list=[int(x) for x in range(1,20) if x%2==0]
print(list)