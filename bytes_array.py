list1=[10,20,40]
print(type(list1))
#convertig list data type to byte using byte build in function but it converts only integer value
b=bytes(list1)
print(type(b))
#bytes object does not support item assignment
b[1]=10
#converting byte type to byte using bytearray build in function but it converts only integer value
b1=bytearray(list1)
print(type(b1))
print(b1[0])
print(b1)
b1[2]=18

