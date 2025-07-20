## Python calculator
operator = input("Enter operator(+,-,*,/,%,**): ")
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

if operator == "+":
    print(f"{num1} {operator} {num2} is {num1+num2}.")
elif operator == "-":
    print(f"{num1} {operator} {num2} is {num1-num2}.")
elif operator == "*":
    print(f"{num1} {operator} {num2} is {num1*num2}.")
elif operator == "/":
    print(f"{num1} {operator} {num2} is {num1/num2}.")
elif operator == "%":
    print(f"{num1} {operator} {num2} is {num1%num2}.")
else:
    print(f"{operator} is not valid. Enter Valid Operator")