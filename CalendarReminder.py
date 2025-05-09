import datetime

all_reminder = []

class Reminder:
    def __init__(self, date, event):
        self.date = date
        self.event = event

def create_reminder():
    date_input = input("Enter the reminder date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        event = input("Enter the reminder event: ")
        reminder_data = {
            'date': date,
            'text': event
        }
        all_reminder.append(reminder_data)
        print("Reminder added successfully!")
    except:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_calendar():
    if not all_reminder:
        print("No reminders available.")
    else:
        print("Reminders:")
        for index, task in enumerate(all_reminder, start=1):
            print(f"{index}. [{task['date']}] - {task['text']}")

def delete_reminder():
    if not all_reminder:
        print("No reminders to delete.")
    else:
        view_calendar()
        try:
            reminder_index = int(input("Enter the number of the reminder to delete: "))
            removed = all_reminder.pop(reminder_index - 1)
            print(f"Reminder '{removed['text']}' removed successfully.")
        except (IndexError, ValueError):
            print("Invalid reminder number. Please try again.")

def edit_reminder():
    if not all_reminder:
        print("No reminders to edit.")
        return

    view_calendar()
    try:
        index = int(input("Enter the number of the reminder you want to edit: ")) - 1
        reminder = all_reminder[index]
    except (IndexError, ValueError):
        print("Invalid reminder number.")
        return

    print("What do you want to edit?")
    print("1. Date")
    print("2. Event text")
    print("3. Both")
    choice = input("Choose (1/2/3): ")

    if choice == "1" or choice == "3":
        new_date_input = input("Enter new date (YYYY-MM-DD): ")
        try:
            new_date = datetime.datetime.strptime(new_date_input, "%Y-%m-%d").date()
            reminder['date'] = new_date
        except:
            print("Invalid date format. Skipping date change.")

    if choice == "2" or choice == "3":
        new_text = input("Enter new event text: ")
        reminder['text'] = new_text

    print("Reminder updated successfully!")

def main():
    while True:
        print("""
=== Calendar Reminder Menu ===
1. Add a new reminder
2. View all reminders
3. Edit a reminder
4. Delete a reminder
5. Exit
        """)
        try:
            option = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
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
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
