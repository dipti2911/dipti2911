def insertionSort(nlist):

     for index in range(1,len(nlist)):
         currentvalue=nlist[index]
         position=index

         while position>0 and nlist[position-1]>currentvalue:
            nlist[position]=nlist[position-1]
            position=position-1
         nlist[position]=currentvalue

nlist=[12,14,45,10,34,18]
insertionSort(nlist)
print(nlist)