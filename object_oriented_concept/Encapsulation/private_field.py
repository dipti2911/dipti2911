class student:
    def __init__(self):
        self.__name="Mahendra"
        self.__id=12
    def dispalay(self):
        print(self.__name)
        print(self.__id)
s=student()
s.dispalay()
print(s.__student__id);#print the private field using class name and private field name

"""_variable name -: this syntax makes the variable as private field
if we want to access those fields then create the method and print those 
field in that method and called the method using the object of that class"""
