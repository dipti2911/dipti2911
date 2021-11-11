import mymath
print(mymath.sum(10,5))
print(mymath.mult(4,6))

#**************Different way to import module***********************

import mymath as m
print(m.sum(12,6))
print(m.mult(2,5))

#*******************************************************************
from  mymath import *
print(sum(12.6,45.2))
print(mult(12.9,67.9))