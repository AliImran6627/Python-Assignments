name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))
numberList = [num1, num2, num3]

print(f"Hey, {name}! Let's explore your favorite numbers:")
TupleList = []
for x in numberList:
    if (x%2) == 0:
        TupleList.append((x, "Even"))
    else:
        TupleList.append((x, "Odd"))
squareTuples = []
for number, info in TupleList:
    squareTuples.append((number, number ** 2))
for number, square in squareTuples:
    print(f"The number is {number}, and its square is {square}.")
NumSum = sum(numberList)
print(f"The sum of the numbers is {NumSum}.")

prime = True
if NumSum > 1:
    for x in range(2, NumSum):
        if (NumSum % x) == 0:
            prime = False
            break
    if prime == False:
        print(f"{NumSum} is not a prime number.")
    else:
        print(f"{NumSum} is a prime number.")
else:
    print(f"{NumSum} is not a prime number.")
#Test commit