def febbo(c):
    a=0
    b=1
    print(a)
    print(b)
    n=c
    for c in range(1,n+1):
        c=a+b
        a=b
        b=c
        print(c)
febbo(5)