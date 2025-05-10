history = []

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return a ** 0.5

def show_menu():
    print("""
Simple Calculator
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Show History
8. Exit
""")

    
def get_2_numbers():
    while True:
        try:
            a = float(input("Enter number: "))
            break
        except ValueError:
            print("That's not a valid number.")
    while True:
        try:
            b = float(input("Enter number: "))
            break
        except ValueError:
            print("That's not a valid number.")
    return a, b
    
def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                a, b = get_2_numbers()
                result = add(a, b)
                print(f"{a} + {b} = {result}")
                history.append(f"{a} + {b} = {result}")

            elif choice == 2:
                a, b = get_2_numbers()
                result = sub(a, b)
                print(f"{a} - {b} = {result}")
                history.append(f"{a} - {b} = {result}")

            elif choice == 3:
                a, b = get_2_numbers()
                result = mul(a, b)
                print(f"{a} * {b} = {result}")
                history.append(f"{a} * {b} = {result}")

            elif choice == 4:
                a, b = get_2_numbers()
                result = div(a, b)
                print(f"{a} / {b} = {result}")
                history.append(f"{a} / {b} = {result}")

            elif choice == 5:
                a, b = get_2_numbers()
                result = power(a, b)
                print(f"{a} ^ {b} = {result}")
                history.append(f"{a} ^ {b} = {result}")

            elif choice == 6:
                while True:
                    try:
                        a = float(input("Enter a number: "))
                        result = square_root(a)
                        print(f"√{a} = {result}")
                        history.append(f"√{a} = {result}")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            elif choice == 7:
                if history:
                    print("\nCalculation History:")
                    for entry in history:
                        print(entry)
                else:
                    print("History is empty.")

            elif choice == 8:
                print("Exiting the program.")
                break

            else:
                print("Please enter a number from 1 to 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()