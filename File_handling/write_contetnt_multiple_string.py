f=open("myfile.py",'w')
print("Enter text('type # when your complete)")
s=''
while s !='#':
    s=input("Enter the content")
    f.write(s)
f.close()