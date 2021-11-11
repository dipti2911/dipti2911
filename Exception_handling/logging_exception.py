try:
    f=open("Myfile","w")
    a,b=[int(x) for x in input("Enter the two numbers:- ").split()]
    logging.info("division in progress")
    c=a/b
    f.write("writing %d into file"%c)
    print(c)

except ZeroDivisionError:
    print("Divide by zero error")
    print("Enter the non zero number")
    logging.error("division by zero")
else:
    print("you have entered non zero number")
finally:
    f.close()
    print("file closed")
    print("After the exception")