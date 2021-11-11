from abc import abstractmethod  , ABC
class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def stud_info(self):
        print("Student information")
    @abstractmethod
    def info(self):
        pass
class student2(student):
    def __init__(self,age,name,roll_no,marks):
        student.__init__(self,name,roll_no,marks)
        self.age=age
    """def display(self):
        print(self.age)"""
    def info(self):
        print("student marks")

class student3(student):
    def __init__(self,BOD,name,roll_no,marks):
        student.__init__(self,name,roll_no,marks)
        self.BOD=BOD
    def display(self):
            print(self.BOD)
    def info(self):
        print("student birth date")
s1=student3("29-11-1998","Dipti Patil",12,78)
print(s1.name)
print(s1.roll_no)
print(s1.marks)

print(s1.BOD)
s1.stud_info()
s1.display()
s2=student("madhuri",12,34)
print(s2.name)
print(s2.roll_no)
print(s2.marks)
s2.info()