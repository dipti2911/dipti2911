emp_detail1={'emp_name':'Bhupesh','emp_no':101,'emp_sal':50000}
emp_detail2={'emp_name':'Dipti','emp_no':102,'emp_sal':40000}
emp_detail3={'emp_name':'Nayana','emp_no':103,'emp_sal':70000}
print(emp_detail1)
print(emp_detail2)
print(emp_detail3)
print(emp_detail1.get('emp_sal'))
#****************************************************************
m=int(input("Enter the number of employee"))
employee={}
for i in range(m):
    name=input("Enter the name")
    salary=input("Enter the salary")
    employee[name]=salary
while true:
    name=input("Enter the name")
    salary=employee.get(name,-1)
    if salary==-1:
        print("Employee does not exist")
    else:
        print("the salary of employee is:-",salary)
