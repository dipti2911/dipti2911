import os,sys
if os.path.isfile('myfile.py'):

    f=open("myfile.py",'r')
    s=f.read()
    print(s)
    f.close()
else:
    print('file does not exist')