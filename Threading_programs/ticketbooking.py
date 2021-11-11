from threading import*
class buy:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        self.l=Lock()
        #self.l=Semasphore
    def booking(self,seatrequested):
        self.l.acquire()
        print("total seats that are available:",self.availableseats)
        if(self.availableseats>=seatrequested):
            print("confirming ticket")
            print("processing payment")
            print("Printing ticket")
            self.availableseats-=seatrequested
        else:
            print("sorry no seats are available")
            self.l.release()
obj= buy(10)
t1=Thread(target=obj.booking,args=(3,))
t2=Thread(target=obj.booking,args=(2,))
t3=Thread(target=obj.booking,args=(3,))
t1.start()
t2.start()
t3.start()