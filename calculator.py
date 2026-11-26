def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Error: unknown operation"

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        print("Result:", calculate(a, b, op))

    except ValueError:
        print("Error: enter numbers only")

    answer = input("Continue? (y/n): ")
    if answer.lower() != "y":
        break
