def custumrange(x ,y):
    while x<y:
        x+=1
        yield x
result=custumrange(10,40)
for i in result:
    print(i)
