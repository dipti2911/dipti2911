student={'dipti':['java','python','c'],'Mahendra':['CCNA','Ruby''Perl'],'Bhupesh':['Embeded System','C Programming']}
keys=student.keys()
for eachkeys in keys:
    print("cource taken by",eachkeys,"are:-")
    for eachcourse in student[eachkeys]:
        print(eachcourse)
