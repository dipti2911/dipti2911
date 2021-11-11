from threading import*;
from time import*;
class Produser:
    def __init__(self):
        self.products=[]
        self.orderplaced=False

    def prodeuce(self):
        for i in range(1,5):
            self.products.append("products"+str(i))
            sleep(1)
            print("item added")
            self.orderplaced=True
class cunsumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        while self.prod.orderplaced==False:
            print("waiting for the orders")
            sleep(0.2)
        print("oeder placed",self.prod.products)
p=Produser()
c=cunsumer(p)
t1=Thread(target=p.prodeuce())
t2=Thread(target=c.consume())
t1.start()
t2.start()