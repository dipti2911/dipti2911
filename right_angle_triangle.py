# Pint the right angle triangle
a=int(input("Enter the number of rows: "))
for i in range(1,a+1):
    print("*"*i)

#print the right angle triangle using other way
a=int(input("Enter the number of rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print('*', end="")
    print("\n")

#print the right angle triangle using the number 1,22,333 up uo n term
a=int(input("Enter the number of rows: "))
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print("\n")


#print the right angle triangle using the number 1,12,123,1234 up uo n term
a=int(input("Enter the number of rows: "))
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print("\n")


#print the left angle triangle(the code is similar to pyramid code the only diff is in print fun space is extra)
n=int(input("Enter the rows"))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    print("* "*i)


