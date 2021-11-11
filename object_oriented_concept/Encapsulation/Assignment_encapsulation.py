class patient:
    def set_id(self,id):
        self.id=id
    def get_id(self):
        return  self.id
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return  self.name
    def set_SSN(self,SSN):
        self.SSN=SSN
    def get_SSN(self):
        return  self.SSN


p1=patient()
p1.set_id(1)
p1.set_name("Jabar")
p1.set_SSN("hospital11")
print(p1.get_id())
print(p1.get_name())
print(p1.set_SSN())
