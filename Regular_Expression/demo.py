import re
s='hello mahi gampu'
k=re.search(r'h\w\w',s)
print(k.group())
