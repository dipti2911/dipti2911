def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner
def num():
    return 5
resultfun=decor(num)
print(resultfun)

#*** @ decor funcion  *********
def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner
@decor
def num():
    return 5

print(num)


#*********************************
def decor(fun):
    def inner(n):
        result=fun(n)
        result+="How are you"
        return result
    return inner
@decor
def name(name):
    return "hello"+name
print(name(" "))