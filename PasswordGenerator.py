import random
import string
from colorama import init, Fore, Style
import time

# Initialize colorama
init()

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def print_header():
    print(f"\n{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.YELLOW}🔐  Professional Password Generator  🔐")
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}\n")

def print_password(password):
    print(f"\n{Fore.GREEN}Generated Password:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 50}")
    print(f"{Fore.WHITE}{password}")
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}\n")

def main():
    print_header()
    
    while True:
        try:
            length = int(input(f"{Fore.CYAN}Enter password length (8-50): {Style.RESET_ALL}"))
            if not 8 <= length <= 50:
                print(f"{Fore.RED}Please enter a length between 8 and 50.{Style.RESET_ALL}")
                continue

            print(f"\n{Fore.CYAN}Password Requirements:{Style.RESET_ALL}")
            use_uppercase = input(f"{Fore.WHITE}Include uppercase letters? (y/n): {Style.RESET_ALL}").lower() == 'y'
            use_lowercase = input(f"{Fore.WHITE}Include lowercase letters? (y/n): {Style.RESET_ALL}").lower() == 'y'
            use_digits = input(f"{Fore.WHITE}Include numbers? (y/n): {Style.RESET_ALL}").lower() == 'y'
            use_special = input(f"{Fore.WHITE}Include special characters? (y/n): {Style.RESET_ALL}").lower() == 'y'

            if not any([use_uppercase, use_lowercase, use_digits, use_special]):
                print(f"{Fore.RED}Please select at least one character type.{Style.RESET_ALL}")
                continue

            print(f"\n{Fore.YELLOW}Generating password...{Style.RESET_ALL}")
            time.sleep(1)  # Add a small delay for effect
            
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print_password(password)

            choice = input(f"{Fore.CYAN}Generate another password? (y/n): {Style.RESET_ALL}")
            if choice.lower() != 'y':
                print(f"\n{Fore.GREEN}Thank you for using the Password Generator!{Style.RESET_ALL}")
                break

        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Program terminated by user.{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()