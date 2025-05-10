from colorama import init, Fore, Style
import os
from datetime import datetime

# Initialize colorama
init()

# Global variables
history = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════╗
║                    {Fore.YELLOW}Professional Calculator{Fore.CYAN}                 ║
╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

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
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    return a ** 0.5

def show_menu():
    menu = f"""
{Fore.GREEN}Available Operations:{Style.RESET_ALL}
{Fore.CYAN}1.{Style.RESET_ALL} Addition
{Fore.CYAN}2.{Style.RESET_ALL} Subtraction
{Fore.CYAN}3.{Style.RESET_ALL} Multiplication
{Fore.CYAN}4.{Style.RESET_ALL} Division
{Fore.CYAN}5.{Style.RESET_ALL} Power
{Fore.CYAN}6.{Style.RESET_ALL} Square Root
{Fore.CYAN}7.{Style.RESET_ALL} Show History
{Fore.CYAN}8.{Style.RESET_ALL} Exit
"""
    print(menu)

def get_2_numbers():
    while True:
        try:
            a = float(input(f"{Fore.YELLOW}Enter first number: {Style.RESET_ALL}"))
            break
        except ValueError:
            print(f"{Fore.RED}That's not a valid number.{Style.RESET_ALL}")
    while True:
        try:
            b = float(input(f"{Fore.YELLOW}Enter second number: {Style.RESET_ALL}"))
            break
        except ValueError:
            print(f"{Fore.RED}That's not a valid number.{Style.RESET_ALL}")
    return a, b

def format_result(operation, a, b=None, result=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if b is None:
        return f"{timestamp} | {operation} {a} = {result}"
    return f"{timestamp} | {a} {operation} {b} = {result}"

def main():
    while True:
        clear_screen()
        print_banner()
        show_menu()
        try:
            choice = int(input(f"{Fore.YELLOW}Enter your choice (1-8): {Style.RESET_ALL}"))
            
            if choice == 1:
                a, b = get_2_numbers()
                result = add(a, b)
                print(f"\n{Fore.GREEN}Result: {a} + {b} = {result}{Style.RESET_ALL}")
                history.append(format_result("+", a, b, result))

            elif choice == 2:
                a, b = get_2_numbers()
                result = sub(a, b)
                print(f"\n{Fore.GREEN}Result: {a} - {b} = {result}{Style.RESET_ALL}")
                history.append(format_result("-", a, b, result))

            elif choice == 3:
                a, b = get_2_numbers()
                result = mul(a, b)
                print(f"\n{Fore.GREEN}Result: {a} × {b} = {result}{Style.RESET_ALL}")
                history.append(format_result("×", a, b, result))

            elif choice == 4:
                a, b = get_2_numbers()
                result = div(a, b)
                print(f"\n{Fore.GREEN}Result: {a} ÷ {b} = {result}{Style.RESET_ALL}")
                history.append(format_result("÷", a, b, result))

            elif choice == 5:
                a, b = get_2_numbers()
                result = power(a, b)
                print(f"\n{Fore.GREEN}Result: {a} ^ {b} = {result}{Style.RESET_ALL}")
                history.append(format_result("^", a, b, result))

            elif choice == 6:
                while True:
                    try:
                        a = float(input(f"{Fore.YELLOW}Enter a number: {Style.RESET_ALL}"))
                        result = square_root(a)
                        print(f"\n{Fore.GREEN}Result: √{a} = {result}{Style.RESET_ALL}")
                        history.append(format_result("√", a, result=result))
                        break
                    except ValueError:
                        print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")

            elif choice == 7:
                if history:
                    print(f"\n{Fore.CYAN}Calculation History:{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
                    for entry in history:
                        print(f"{Fore.YELLOW}{entry}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
                else:
                    print(f"\n{Fore.YELLOW}History is empty.{Style.RESET_ALL}")

            elif choice == 8:
                print(f"\n{Fore.GREEN}Thank you for using the Professional Calculator!{Style.RESET_ALL}")
                break

            else:
                print(f"\n{Fore.RED}Please enter a number from 1 to 8.{Style.RESET_ALL}")

            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

        except ValueError:
            print(f"\n{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()