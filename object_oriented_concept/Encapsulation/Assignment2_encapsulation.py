class patient:
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return  self.__id
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return  self.__name
    def set_SSN(self,SSN):
        self.__SSN=SSN
    def get_SSN(self):
        return  self.__SSN



p1=patient()
p1.set_id(1)
p1.set_name("Jabar")
p1.set_SSN("hospital11")
print(p1.get_id())
print(p1.get_name())
print(p1.get_SSN())
