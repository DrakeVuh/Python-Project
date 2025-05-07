import random
from colorama import init, Fore, Style
import time

# Initialize colorama
init()

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{text}{Style.RESET_ALL}")

def get_user_choice():
    print_colored("\nChoose your weapon:", Fore.CYAN)
    print_colored("1. Rock", Fore.YELLOW)
    print_colored("2. Paper", Fore.YELLOW)
    print_colored("3. Scissors", Fore.YELLOW)
    
    choice_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice in choice_map:
            return choice_map[choice]
        print_colored("Invalid choice. Please enter 1, 2, or 3.", Fore.RED)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def display_round_result(user_choice, computer_choice, result, score):
    print_colored("\n" + "="*50, Fore.BLUE)
    print_colored(f"Your choice: {user_choice.upper()}", Fore.GREEN)
    print_colored(f"Computer's choice: {computer_choice.upper()}", Fore.RED)
    print_colored(f"Result: {result}", Fore.YELLOW)
    print_colored("="*50, Fore.BLUE)

def display_final_score(user_score, computer_score, rounds):
    print_colored("\n" + "="*50, Fore.MAGENTA)
    print_colored("GAME SUMMARY", Fore.MAGENTA, Style.BRIGHT)
    print_colored(f"Total Rounds: {rounds}", Fore.CYAN)
    print_colored(f"Your Score: {user_score}", Fore.GREEN)
    print_colored(f"Computer's Score: {computer_score}", Fore.RED)
    
    if user_score > computer_score:
        print_colored("Congratulations! You are the overall winner! 🎉", Fore.GREEN, Style.BRIGHT)
    elif computer_score > user_score:
        print_colored("Computer wins the game! Better luck next time!", Fore.RED)
    else:
        print_colored("The game ended in a tie!", Fore.YELLOW)
    print_colored("="*50, Fore.MAGENTA)

def main():
    print_colored("\n" + "="*50, Fore.CYAN)
    print_colored("Welcome to Rock, Paper, Scissors!", Fore.CYAN, Style.BRIGHT)
    print_colored("A Classic Game of Strategy and Luck", Fore.CYAN)
    print_colored("="*50, Fore.CYAN)
    
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result, score = determine_winner(user_choice, computer_choice)
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1
            
        display_round_result(user_choice, computer_choice, result, score)
        
        play_again = input("\nWould you like to play another round? (y/n): ").lower()
        if play_again != 'y':
            break
    
    display_final_score(user_score, computer_score, rounds)
    print_colored("\nThank you for playing! Goodbye!", Fore.CYAN)

if __name__ == "__main__":
    main()