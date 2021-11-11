import pickle,student
f=open('student.dat','wb')
s=student.student(12,'dipti',56)
pickle.dump(s,f)
f.close()
