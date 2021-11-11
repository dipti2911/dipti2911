class product:
    def __init__(self):
        self.name='Lenovo'
        self.id=101
        self.price=50000
p1=product()
print(p1.name)
print(p1.id)
print(p1.price)




class student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
s1=student("dipti",12,56)
print(s1.name)
print(s1.roll_no)
print(s1.marks)