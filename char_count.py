s='aabbnioprreti'
p={}
for c in s:
    if c in p.keys():
        p[c]=p[c]+1
    else:
        p[c]=1
for k,v in p.items():
    print('{}={} times'.format(k,v))