print("product of list number")
list=[1,2,3,4,5]
prod=1
for i in list:
    prod*=i
    print(prod)#print output at every iteration
print("product of list",prod)#print output only once

print("\n Factorial of given number")
a=int(input("Enter the number"))
fact=1
if a==0:
    print("factorial of 0 is 1")
n=a
for a in range(1,n+1):
    fact=fact*a
print(fact)

print("\n***********Febbonenci series**********")
a=int(input("enter the number"))
b=0
c=1
print(b)
print(c)
n=a
for a in range(1,n+1):
    a=b+c
    b=c
    c=a
    print(a)

print("\n*********Multiplication table of given number***********")
no=int(input("Enter the number which you want to display the table"))
for l in range(1,11):
    a=no*l
    print(a)










