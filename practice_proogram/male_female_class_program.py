class Person:
    def getGender(self,gender):
        self.gender=gender
class male(Person):
    def getGender(self):
        print("male")
class female(Person):
    def getGender(self):
        print("female")
f=female()
f.getGender()
m=male()
m.getGender()



