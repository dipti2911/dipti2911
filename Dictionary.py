dict={'name':"Bhupesh",'age':25,'bd':'18-5-1995'}
print(dict)
print(dict.keys())


k=dict.keys()
for i in k:
    print(i)

print('\n')
v=dict.values()
for i in v:
    print(i)
print(dict.items())
#print(dict)
print('---------------------------------------')
print(dict.copy())
y='mahi'
print('---------------------------------------')
print(dict.fromkeys(dict,y))
print(dict.pop('age'))
print(dict.get('bd'))
print(dict.popitem())
print(dict)
dict1={'age':'26'}
dict.update(dict1)
print(dict)
