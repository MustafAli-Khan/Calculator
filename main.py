import art

print(art.logo)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(art.logo)
    n1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick a operation : ")
        n2 = float(input("What's the next number: "))

        calci_function = operations[operation_symbol]
        answer = calci_function(a=n1, b=n2)

        print(f"{n1}{operation_symbol}{n2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation : ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()