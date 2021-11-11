from threading import*
from time import  sleep
class mythread():
    def displaynum(self):
        i = 0
        print(current_thread().getName())
        sleep(1)
        while (i <= 10):
            print(i)
            i += 1

obj=mythread()
t=Thread(target=obj.displaynum())
t.start()

t1=Thread(target=obj.displaynum())
t1.start()


t2=Thread(target=obj.displaynum())
t2.start()