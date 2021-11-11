
from datetime import date
import time
starttime=time.perf_counter()
ldates=[]
d1=date(2016,12,4)
d2=date(2018,12,4)
d3=date(2015,12,4)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.sort()

for d in ldates:
    print(d)
endtime=time.perf_counter()
print("Execution time",endtime-starttime)