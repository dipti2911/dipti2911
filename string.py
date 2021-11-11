s1="    dipti  "
print(s1)

s2="""I
LOVE
YOU
MAHIIII"""
#print string multiple times
print(s1*2)

#slicing string
print(s2[11:15])
print((len(s1)))

print(s1[:-2])

print(s2 [::-1])

print(s2[:])
#strip string function to remove space

print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

#string function
print("STRING FUNCTION")

print(s1.count("i"))
print(s1.find("Love",0,len(s2)))
print(s2.find("L",0,6))
print(s1.find("you"))
print(s1.replace("ti","mahi"))
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s2.title())
print(s2.find("MAHI"))



