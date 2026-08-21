first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

while True:
    operator = input("Choose an operator (+, -, *, /): ")
    if operator in ("+", "-", "*", "/"):  # little check
        break
    print("Error: operator must be +, -, * or /.")

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
else:  # operator "/"
    if second == 0:  # little check
        print("Error: division by zero is not allowed.")
        result = None
    else:
        result = first / second

print(f"Result: {first} {operator} {second} = {result}")
