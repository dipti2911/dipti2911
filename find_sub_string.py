a="dipti patil at post dhamodi tal raver dist jalgoan"
subs='dist'
found=False
pos=-1
length=len(a)
while True:
    pos=a.find(subs,pos+1,length)
    if pos==-1:
        break
    print("found the substring at position ",pos)
    found=True
    if found==False:
        print("substring does not found")

