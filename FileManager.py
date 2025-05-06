task = []


def show_menu():
    print("""
===== FILE MANAGER MENU =====
1. Add Task.
2. View Tasks.
3. Mark Task as Completed.
4. Delete Task.
5. Exit.
    """)

def add_task():
    new_task = input("Enter the task you have to do: ")
    task.append(new_task)
    print("Task added successfully!")

def view_task():
    for index, item in enumerate(task, start = 1):
        print(f"{index}. {item}")

def delete_task():
    if not task:
        print("No tasks to delete.")
    view_task()
    try:
        del_task = int(input("Enter the number of the task to delete:"))
        task.pop(del_task - 1)
    except:
        print("The task number is invalid!!! Please try again!!!")


def Completed():
    if not task:
        print("No tasks to delete.")
    view_task()
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if task[num -1].endswith("[Done]"):
            print("You already did this!!!")
        else:
            task[num - 1] =  task[num - 1] + " [Done]"
    except:
        print("The task number is invalid!!! Please try again!!!")

def main():
    show_menu()
    while True:
        user_choice = int(input("Enter option you want to do: "))
        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            view_task()
        elif user_choice == 3:
            Completed()
        elif user_choice == 4:
            delete_task()
        elif user_choice == 5:
            exit()

if __name__ == "__main__":
    main()