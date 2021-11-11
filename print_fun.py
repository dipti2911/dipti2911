print("helloo")
print("Bhupesh*2")
print("I LOVE YOU MAHI \n DIPAAAA")
print(12,23)
print(12,34,sep=",")
print(12,78,sep="+++")

Name="Dipti"
Marks=67.90
print(Name,Marks)
print("Name is- ",Name,"Marks are- ",Marks)
print("Name is %s ,Marks are %2f"%(Name,Marks))
print("Name is {},Marks are {}".format(Name,Marks))
print("Name is {0},Marks are {1}".format(Name,Marks))

#********************************************************#
print("\n")
s=input("Enter your Name- ")
print(s)
print(type(s))

i=int(input("Enter integer value- "))
print(i)
print(type(i))

#*********Multiple input**********************************#

Marks =input("Enter the Marks")
print(Marks)

lst=[x for x in input("Enter the Marks seperated by space:-").split()]
print(lst)


lst=[int(x) for x in input("Enter the Marks seperated by comma:-").split(",")]
print(lst)


