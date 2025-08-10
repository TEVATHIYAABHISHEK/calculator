def add(n1, n2):
    return n1 + n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return n1 / n2
def sub(n1, n2):
    return n1 - n2

operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

while True:
    num1 = get_number("what is the first number :")
    print("Available operations:", " ".join(operations.keys()))
    operation_symbol = input("Pick an operation from the line above: ")
    if operation_symbol not in operations:
        print("Invalid operation. Try again.")
        continue
    num2 = get_number("what is the second number :")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    if answer is not None:
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    else:
        continue

    choice = input("Type 'y' to continue calculating with the result, or 'n' to start over, or any other key to exit: ")
    if choice == 'y':
        while choice == 'y':
            num1 = answer
            print("Available operations:", " ".join(operations.keys()))
            operation_symbol = input("Pick an operation from the line above: ")
            if operation_symbol not in operations:
                print("Invalid operation. Try again.")
                continue
            num2 = get_number("what is the next number :")
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            if answer is not None:
                print(f"{num1} {operation_symbol} {num2} = {answer}")
            else:
                break
            choice = input("Type 'y' to continue calculating with the result, or 'n' to start over, or any other key to exit: ")
        if choice == 'n':
            continue
        else:
            print("Thank you for using the calculator!")
            break
    elif choice == 'n':
        continue
    else:
        print("Thank you for using the calculator!")
        break