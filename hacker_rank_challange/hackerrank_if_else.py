n=int(input("Enter the number"))
if n%2==1:
    print("weird")
elif n%2==0 and 2<=n<=6:
    print("Not weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
else:
    print("not weird")
