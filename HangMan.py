import random
import sys

# ANSI color codes for terminal output
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"

# Hangman ASCII art stages
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
   =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
   =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
   =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
   =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
   =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
   =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
   =========
    """
]

MAX_ATTEMPTS = len(HANGMAN_PICS) - 1


def get_random_word():
    """Return a random word from the list."""
    words = [
        "python", "java", "javascript", "ruby", "php", "swift", "kotlin", "go", "rust", "scala"
    ]
    return random.choice(words)


def initialize_game(word):
    """Initialize the game state."""
    guessed_letters = []
    attempts = MAX_ATTEMPTS
    hidden_word = ["_" for _ in word]
    return guessed_letters, attempts, hidden_word


def display_game(guessed_letters, attempts, hidden_word):
    """Display the current game state with ASCII art and colors."""
    print("\n" + BOLD + CYAN + "=== Hangman Game ===" + RESET)
    print(HANGMAN_PICS[MAX_ATTEMPTS - attempts])
    print(f"{YELLOW}Attempts Remaining:{RESET} {BOLD}{attempts}{RESET}")
    print(f"{YELLOW}Guessed Letters:{RESET} {', '.join(guessed_letters) if guessed_letters else '-'}")
    print(f"{YELLOW}Word:{RESET} {BOLD}{' '.join(hidden_word)}{RESET}")
    print("-" * 30)


def get_player_guess(guessed_letters):
    """Prompt the player for a guess and validate input."""
    while True:
        guess = input(f"{CYAN}Guess a letter: {RESET}").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{YELLOW}You already guessed that letter.{RESET}")
            else:
                return guess
        else:
            print(f"{RED}Please enter a valid single letter.{RESET}")


def update_hidden_word(word, hidden_word, guess):
    """Reveal guessed letters in the hidden word."""
    return [guess if word[i] == guess else hidden_word[i] for i in range(len(word))]


def main():
    """Main function to run the Hangman game."""
    print(BOLD + GREEN + "Welcome to Professional Hangman!" + RESET)
    word = get_random_word()
    guessed_letters, attempts, hidden_word = initialize_game(word)

    while attempts > 0 and "_" in hidden_word:
        display_game(guessed_letters, attempts, hidden_word)
        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(GREEN + BOLD + "Correct!" + RESET)
            hidden_word = update_hidden_word(word, hidden_word, guess)
        else:
            print(RED + BOLD + "Wrong!" + RESET)
            attempts -= 1

    display_game(guessed_letters, attempts, hidden_word)

    if "_" not in hidden_word:
        print(GREEN + BOLD + f"🎉 You won! The word was: {word}" + RESET)
    else:
        print(RED + BOLD + f"💀 Game over! The word was: {word}" + RESET)
    print(BOLD + CYAN + "Thanks for playing!" + RESET)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "Game interrupted. Goodbye!" + RESET)
        sys.exit(0)
