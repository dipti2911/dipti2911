s1={12,34,23,1,'mayur'}
print(s1)

print(type(s1))
#set does not support slicing


#In set their is no indexing if we add element in set they are added in set in any location
s1.update([10,45])
print(s1)
s1.remove(12)
print(s1)

print(s1[0:3])
#in set if we want to print element using indexing it is not possible
print(s1[1])

#frozen set - if we made the set to frozen set then not able to update or remove
f=frozenset(s1)
print(s1)
f.remove(45)
print(f)