
num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]


while True:
    if reset == True:
        num = int(input("Enter the starting number: "))
        reset = False

    operation = input("Enter an arithmetic operation " + str(calcOperations) + " or type 'exit' to quit or 'reset' to start over: ")

    if operation == "exit":
        break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("Invalid operation entered.")
        continue


    secondNum = int(input("Enter the second number: "))

    if operation == "+":
        result = num + secondNum
    elif operation == "-":
        result = num - secondNum
    elif operation == "*":
        result = num * secondNum
    elif operation == "/":
        result = num / secondNum
    elif operation == "**":
        result = num ** secondNum


    print("Result: " + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))

    num = result
    result = None