def myfunction(x,*args,**kwargs):
    for each_args in args:
        print(each_args)
    for key,value in kwargs.items():
        print(key,value)

myfunction(10,20,30,name="dipti",address="Dhamodi")