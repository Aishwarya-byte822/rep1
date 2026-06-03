def add_numbers():
    pass

def subtract_numbers():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        res = a - b
        print("Result : ", res)
    except ValueError:
        print("Error : Please enter valid integers!")

def multiply_numbers():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        res = a * b
        print("Result : ", res)
    except ValueError:
        print("Error : Please enter valid integers!")


def power_numbers():
    try:
        a = int(input("Enter base number : "))
        b = int(input("Enter exponent : "))
        res = a ** b
        print("Result :", res)
    except ValueError:
        print("Error : Please enter valid integers!")


def modulo_numbers():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        res = a % b
        print("Result :", res)
    except ValueError:
        print("Error : Please enter valid integers!")
    except ZeroDivisionError:
        print("Error : Modulo by zero not allowed!")


def floor_division_numbers():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        res = a // b
        print("Result :", res)
    except ZeroDivisionError:
        print("Error : Division by zero not allowed!") 

def divide_numbers():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    try:
        res=a / b
        print("Result : ",res)
    except ZeroDivisionError:
        print("Error : Division by zero not allowed!")

while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulo")
    print("7. Floor Division")
    print("0. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            add_numbers()

        case "2":
            subtract_numbers()

        case "3":
            multiply_numbers()

        case "4":
            divide_numbers()

        case "5":
            power_numbers()

        case "6":
            modulo_numbers()

        case "7":
            floor_division_numbers()

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice")

            

