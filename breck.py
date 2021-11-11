print("\n breck")
list=[1,3,4,5,6]
for i in list:
    if i==5:
        break
    print(i)

print("\n continue")
list=[1,3,4,5,6]
for i in list:
    if i==5:
        continue
    print(i)
#print 1 to 20 and skip multiple of 3 using for loop
print("\n")
for no in range(1,21):
        if no%3==0:
            continue
        print(no)

# print 1 to 20 and skip multiple of 3 using while loop
print("\n")
x=0
while x<20:
    x=x+1
    if x%3==0:
        continue
    print(x)






