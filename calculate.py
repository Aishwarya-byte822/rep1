def add_numbers():
    pass

def subtract_numbers():
    pass

def multiply_numbers():
    pass

def divide_numbers():
    pass


while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
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

        case "0":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice")

