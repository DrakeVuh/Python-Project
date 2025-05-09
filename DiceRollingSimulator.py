import random

def _roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")
        result = _roll_dice()
        print(f"You rolled a {result}")

        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice == "y":
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()