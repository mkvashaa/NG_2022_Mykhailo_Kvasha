FirstNum = int(input("Enter the first number: "))
Operation = str(input("Enter the operation: "))
SecondNum = int(input("Enter the second number: "))

if (Operation == "+"):
    print(FirstNum, "+", SecondNum, "=", FirstNum+SecondNum)
if (Operation == "-"):
    print(FirstNum, "-", SecondNum, "=", FirstNum-SecondNum)
if (Operation == "*"):
    print(FirstNum, "*", SecondNum, "=", FirstNum*SecondNum)
if (Operation == "/"):
    print(FirstNum, "/", SecondNum, "=", FirstNum/SecondNum)
