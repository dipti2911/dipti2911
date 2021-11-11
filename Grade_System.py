sub=['math','physics','chemistry']
print(sub)
math=int(input("Enter marks"))
print(math)
physics=int(input("Enter marks"))
print(physics)
chemistry=int(input("Enter marks"))
print(chemistry)
Total=math+physics+chemistry
average=Total/3
print(Total)
print(average)

if average<35:
    print('Fail')
elif average<=59:
    print('Grade','C')
elif average<=69:
    print('Grade','B')
else:
    print('Grade','A')
