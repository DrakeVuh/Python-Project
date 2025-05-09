import datetime

# ANSI color codes for beautifying terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

all_reminders = []

class Reminder:
    """A class to represent a reminder."""
    def __init__(self, date, event):
        self.date = date
        self.event = event

def print_separator():
    print(f"{Colors.OKBLUE}{'-'*40}{Colors.ENDC}")

def save_reminders_to_file():
    """Save all reminders to Reminder.txt in a readable format."""
    with open("Reminder.txt", "w") as f:
        if not all_reminders:
            f.write("No reminders available.\n")
        else:
            f.write(f"{'No.':<5}{'Date':<15}{'Event'}\n")
            for index, task in enumerate(all_reminders, start=1):
                f.write(f"{index:<5}{str(task['date']):<15}{task['text']}\n")

def create_reminder():
    """Create a new reminder and add it to the list."""
    print_separator()
    print(f"{Colors.HEADER}{Colors.BOLD}Add a New Reminder{Colors.ENDC}")
    date_input = input("Enter the reminder date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        event = input("Enter the reminder event: ")
        reminder_data = {
            'date': date,
            'text': event
        }
        all_reminders.append(reminder_data)
        print(f"{Colors.OKGREEN}Reminder added successfully!{Colors.ENDC}")
        save_reminders_to_file()
    except ValueError:
        print(f"{Colors.FAIL}Invalid date format. Please use YYYY-MM-DD.{Colors.ENDC}")

def view_calendar():
    """Display all reminders in a formatted list."""
    print_separator()
    print(f"{Colors.HEADER}{Colors.BOLD}All Reminders{Colors.ENDC}")
    if not all_reminders:
        print(f"{Colors.WARNING}No reminders available.{Colors.ENDC}")
    else:
        print(f"{Colors.UNDERLINE}{'No.':<5}{'Date':<15}{'Event'}{Colors.ENDC}")
        for index, task in enumerate(all_reminders, start=1):
            print(f"{index:<5}{str(task['date']):<15}{task['text']}")

def delete_reminder():
    """Delete a reminder by its index."""
    print_separator()
    print(f"{Colors.HEADER}{Colors.BOLD}Delete a Reminder{Colors.ENDC}")
    if not all_reminders:
        print(f"{Colors.WARNING}No reminders to delete.{Colors.ENDC}")
    else:
        view_calendar()
        try:
            reminder_index = int(input("Enter the number of the reminder to delete: "))
            removed = all_reminders.pop(reminder_index - 1)
            print(f"{Colors.OKGREEN}Reminder '{removed['text']}' removed successfully.{Colors.ENDC}")
            save_reminders_to_file()
        except (IndexError, ValueError):
            print(f"{Colors.FAIL}Invalid reminder number. Please try again.{Colors.ENDC}")

def edit_reminder():
    """Edit the date, event, or both for a selected reminder."""
    print_separator()
    print(f"{Colors.HEADER}{Colors.BOLD}Edit a Reminder{Colors.ENDC}")
    if not all_reminders:
        print(f"{Colors.WARNING}No reminders to edit.{Colors.ENDC}")
        return

    view_calendar()
    try:
        index = int(input("Enter the number of the reminder you want to edit: ")) - 1
        reminder = all_reminders[index]
    except (IndexError, ValueError):
        print(f"{Colors.FAIL}Invalid reminder number.{Colors.ENDC}")
        return

    print("What do you want to edit?")
    print(f"{Colors.OKCYAN}1. Date\n2. Event text\n3. Both{Colors.ENDC}")
    choice = input("Choose (1/2/3): ")

    if choice == "1" or choice == "3":
        new_date_input = input("Enter new date (YYYY-MM-DD): ")
        try:
            new_date = datetime.datetime.strptime(new_date_input, "%Y-%m-%d").date()
            reminder['date'] = new_date
        except ValueError:
            print(f"{Colors.FAIL}Invalid date format. Skipping date change.{Colors.ENDC}")

    if choice == "2" or choice == "3":
        new_text = input("Enter new event text: ")
        reminder['text'] = new_text

    print(f"{Colors.OKGREEN}Reminder updated successfully!{Colors.ENDC}")
    save_reminders_to_file()

def main():
    while True:
        print_separator()
        print(f"{Colors.BOLD}{Colors.OKBLUE}=== Calendar Reminder Menu ==={Colors.ENDC}")
        print(f"{Colors.OKCYAN}1. Add a new reminder\n2. View all reminders\n3. Edit a reminder\n4. Delete a reminder\n5. Exit{Colors.ENDC}")
        print_separator()
        try:
            option = int(input("Enter your choice (1-5): "))
        except ValueError:
            print(f"{Colors.FAIL}Invalid input. Please enter a number.{Colors.ENDC}")
            continue

        if option == 1:
            create_reminder()
        elif option == 2:
            view_calendar()
        elif option == 3:
            edit_reminder()
        elif option == 4:
            delete_reminder()
        elif option == 5:
            print(f"{Colors.OKGREEN}Goodbye!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.WARNING}Please choose a valid option (1-5).{Colors.ENDC}")

if __name__ == "__main__":
    main()
