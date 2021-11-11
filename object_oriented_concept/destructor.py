class product:
    def __init__(self):
        self.name='Lenovo'
        self.id=101
        self.price=50000
    def __del__(self):
        print("inside destructor")
    def display(self):
        print(self.name)
        print(self.id)
        print(self.price)
p1=product()
p1.display()
p1=None
