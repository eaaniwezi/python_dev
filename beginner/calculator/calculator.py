from calculator_logo import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True


    while should_continue:
        operations_type = input("Operations type do you want? ")
        num2 = float(input("What is the next number?: "))
        function = operations[operations_type]
        result = function(num1, num2)

        print(f"{num1} {operations_type} {num2} = {result}") 
        wanna_continue = input("Do you want to continue? Yes or No").lower()
        
        if wanna_continue == 'no':
            should_continue = False
            calculator()
        else:
            num1 = result


calculator()