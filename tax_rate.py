# find the tax rate
salary = float(input("Enter your salary : "))
if (salary < 30000):
    print("Tax rate = 5%")
    tax = salary *0.05
    salary2 = salary - tax
    print("Your final salary : ",salary2)

elif (salary >= 30000 and salary < 70000):
    print("Tax rate = 15%")
    tax = salary *0.15
    salary2 = salary - tax
    print("Your final salary : ",salary2)

elif (salary >= 70000):
    print("Tax rate = 25%")
    tax = salary *0.25
    salary2 = salary - tax
    print("Your final salary : ",salary2)

else :
    print("Invalid ammount")