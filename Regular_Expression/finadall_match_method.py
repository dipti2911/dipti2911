import re
s='hello 66 hello 55 mahi gampu 23-4-1994'
k=re.search(r'h\w',s)
print(k.group())

k=re.findall(r'h\w',s)
print(k)

k=re.match(r'h\w',s)
print(k.group())

k=re.split(r'\d+',s)
print(k)

k=re.sub(r'mahi','dipti',s)
print(k)

k=re.findall(r'h\w+',s)
print(k)

k=re.findall(r'h\w?',s)
print(k)

k=re.findall(r'h\w*',s)
print(k)

k=re.findall(r'h\w{2}',s)
print(k)

k=re.findall(r'h\w{1,3}',s)
print(k)

k=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',s)
print(k)


k=re.findall(r'^h\w*',s)
print(k)