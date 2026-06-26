




# BETTER CALCULATOR
num1 = float(input("Enter Number: "))
op = input("Select an icon>> (+, -, *,/): ")
num2 = float(input("Enter Numper: "))
def Calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Error Select an icon>> (+, -, *,/): "

Calculation = Calculator(num1, op, num2)

print(Calculation)