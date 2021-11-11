def factorial(no):
    fact=1
    if no==0:
        print("factorial of the given no is: ",fact)
    else:
        for no in range(1,no+1):
            fact=fact*no
        print(fact)
factorial(5)


