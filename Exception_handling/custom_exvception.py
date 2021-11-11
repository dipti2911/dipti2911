class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdraw(amount):
    if(amount>500):
        print("You cannot withdraw more than 500rs")
withdraw(600)


#*****************************************************

class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
age=int(input("Enter the age:-"))
if age<18:
    raise TooYoungException("you have to be 18 or older to apply")
elif age>90:
    raise TooOldException("you have to be younger than 90")
else:
    print("you are eligible:-")