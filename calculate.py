def add_numbers():
    pass

def subtract_numbers():
    pass

def multiply_numbers():
    pass

def divide_numbers():
    pass

def power_numbers():
    pass

def modulo_numbers():
    pass

def floor_division_numbers():
    pass


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

            

