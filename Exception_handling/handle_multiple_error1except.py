def fun(a):
    if a<2:
        b=a/(a-2)
    print("value of b is-",b)
try:
    fun(3)
    fun(4)
    fun(7)

except ZeroDivisionError:
    print("divide by zero error is occured")
except NameError:
    print("Name error occured handled")