value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")
op = input("Enter operation(+,-,*,/): ")
if op == "+":
    print("The Sum of the numbers is: ", float(value1) + float(value2))
elif op == "-":
    print("The Difference of the numbers is: ", float(value1) - float(value2))
elif op == "*":
    print("The Product of the numbers is: ", float(value1) * float(value2))
elif op == "/" and float(value2) != 0:
    print("The quotient after division is: ",  float(value1) / float(value2))
else:
    print("Invalid operation or attempt to divide by zero")