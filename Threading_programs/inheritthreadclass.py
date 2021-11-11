from threading import Thread
class mythread(Thread):
    def run(self):
        i=0
        while(i<=10):
            print(i)
            i+=1
t=mythread()
t.run()
