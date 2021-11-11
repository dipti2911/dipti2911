import datetime
import time
epochseconds=time.time()
print(epochseconds)

t=time.ctime(epochseconds)
print(t)


dt=datetime.datetime.today()
print("Current date:{}/{}/{} ".format(dt.day,dt.month,dt.year))
print("Current time:{}:{}:{} ".format(dt.hour,dt.minute,dt.second))