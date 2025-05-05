import random

MIN_NUMBER = 1
MAX_NUMBER = 100

WELCOME_BANNER = """
========================================
  Welcome to the Number Guessing Game!
========================================
I'm thinking of a number between {min} and {max}.
Can you guess what it is?
""".format(min=MIN_NUMBER, max=MAX_NUMBER)

CONGRATS_ART = r"""
  _____                            _         _       _   _                 
 / ____|                          | |       | |     | | (_)                
| |     ___  _ ____   _____ _ __  | |     __| | __ _| |_ _  ___  _ __  ___ 
| |    / _ \| '_ \ \ / / _ \ '__| | |    / _` |/ _` | __| |/ _ \| '_ \/ __|
| |___| (_) | | | \ V /  __/ |    | |___| (_| | (_| | |_| | (_) | | | \__ \
 \_____\___/|_| |_|\_/ \___|_|    |______\__,_|\__,_|\__|_|\___/|_| |_|___/
"""

def get_user_guess():
    """Prompt the user for a guess and validate the input."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}): "))
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
            else:
                print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def play_game():
    """Main game logic for the number guessing game."""
    random_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print(WELCOME_BANNER)

    while True:
        guess = get_user_guess()
        attempts += 1
        if guess > random_num:
            print("  🔻 Too high, try again!\n")
        elif guess < random_num:
            print("  🔺 Too low, try again!\n")
        else:
            guess_word = "guess" if attempts == 1 else "guesses"
            print(f"\n{CONGRATS_ART}")
            print(f"🎉 You win in {attempts} {guess_word}! Congratulations! 🎉\n")
            break

def main():
    """Entry point for the game."""
    while True:
        play_game()
        replay = input("Would you like to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thank you for playing! Goodbye!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()