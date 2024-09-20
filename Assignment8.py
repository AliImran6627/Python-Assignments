value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")
op = input("Enter the operation you wish to perform(+,-,*,/): ")

def addition(val1,val2):
    return (float(val1)+float(val2))

def subtraction(val1,val2):
    return (float(val1)-float(val2))

def multiplication(val1,val2):
    return(float(val1)*float(val2))

def division(arg1,arg2):
    if float(arg2) != 0:
        return (float(arg1)/float(arg2))
    else:
        print("Error: Attempt to divide by Zero")
        return None

if op == "+":
    print(addition(value1,value2))
elif op == "-":
    print(subtraction(value1,value2))
elif op == "*":
    print(multiplication(value1,value2))
elif op == "/":
    result = (division(value1,value2))
    print("Result: ", result)
else:
    print("Invalid Operation")