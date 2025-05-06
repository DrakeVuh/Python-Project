from datetime import datetime
from colorama import init, Fore, Style
import os
import json

# Initialize colorama
init()

# Global variables
tasks = []
TASK_FILE = "Task_to_do.txt"

def load_tasks():
    try:
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, 'r') as file:
                return json.load(file)
    except Exception as e:
        print(f"{Fore.RED}Error loading tasks: {str(e)}{Style.RESET_ALL}")
    return []

def save_tasks():
    try:
        with open(TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"{Fore.RED}Error saving tasks: {str(e)}{Style.RESET_ALL}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════╗
║         TASK MANAGER v1.0          ║
╠════════════════════════════════════╣
║ {Fore.WHITE}1. Add New Task                    {Fore.CYAN}║
║ {Fore.WHITE}2. View All Tasks                  {Fore.CYAN}║
║ {Fore.WHITE}3. Mark Task as Completed          {Fore.CYAN}║
║ {Fore.WHITE}4. Delete Task                     {Fore.CYAN}║
║ {Fore.WHITE}5. Exit                            {Fore.CYAN}║
╚════════════════════════════════════╝{Style.RESET_ALL}
    """)

def add_task():
    clear_screen()
    print(f"{Fore.CYAN}=== Add New Task ==={Style.RESET_ALL}")
    new_task = input(f"{Fore.GREEN}Enter the task description: {Style.RESET_ALL}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks.append({
        'description': new_task,
        'created_at': timestamp,
        'completed': False
    })
    save_tasks()  # Save tasks after adding
    print(f"\n{Fore.GREEN}✓ Task added successfully!{Style.RESET_ALL}")
    input("\nPress Enter to continue...")

def view_tasks():
    clear_screen()
    print(f"{Fore.CYAN}=== Your Tasks ==={Style.RESET_ALL}\n")
    
    if not tasks:
        print(f"{Fore.YELLOW}No tasks available.{Style.RESET_ALL}")
    else:
        for index, task in enumerate(tasks, start=1):
            status = f"{Fore.GREEN}[✓]{Style.RESET_ALL}" if task['completed'] else f"{Fore.YELLOW}[ ]{Style.RESET_ALL}"
            print(f"{index}. {status} {task['description']}")
            print(f"   {Fore.BLUE}Created: {task['created_at']}{Style.RESET_ALL}")
    
    input("\nPress Enter to continue...")

def mark_completed():
    clear_screen()
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input(f"\n{Fore.GREEN}Enter task number to mark as completed: {Style.RESET_ALL}"))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks()  # Save tasks after marking as completed
            print(f"\n{Fore.GREEN}✓ Task marked as completed!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Invalid task number!{Style.RESET_ALL}")
    except ValueError:
        print(f"\n{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
    
    input("\nPress Enter to continue...")

def delete_task():
    clear_screen()
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input(f"\n{Fore.RED}Enter task number to delete: {Style.RESET_ALL}"))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks()  # Save tasks after deletion
            print(f"\n{Fore.GREEN}✓ Task deleted: {deleted_task['description']}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Invalid task number!{Style.RESET_ALL}")
    except ValueError:
        print(f"\n{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
    
    input("\nPress Enter to continue...")

def main():
    global tasks
    tasks = load_tasks()  # Load tasks when program starts
    while True:
        show_menu()
        try:
            choice = int(input(f"{Fore.CYAN}Enter your choice (1-5): {Style.RESET_ALL}"))
            
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_completed()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print(f"\n{Fore.CYAN}Thank you for using Task Manager!{Style.RESET_ALL}")
                break
            else:
                print(f"\n{Fore.RED}Invalid choice! Please select 1-5.{Style.RESET_ALL}")
                input("\nPress Enter to continue...")
        except ValueError:
            print(f"\n{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()