# CREATE A SIMPLE CALCULATOR
def calculator(a,b,operator):
    if(operator == "+"):
        print(a+b)
    elif(operator == "-"):
        print(a-b)
    elif(operator == "*"):
        print(a*b)
    elif(operator == "/"):
        print(a/b)
    elif(operator == "%"):
        print(a%b)
    else:
        print("Invalid operator")
a = int(input("Enter the first number; "))
b = int(input("Enter the second number: "))
operator = input("+ or - or * or / or % : ")
calculator(a,b,operator)