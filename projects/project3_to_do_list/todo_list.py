# ============================================================
# PROJECT 3: To-Do List
# CONCEPTS: lists, while loops, if/elif/else, functions,
#           def, return, len(), enumerate(), .append().
#           .remove(), string methods
# ============================================================
# A simple command-line to-do list.
# The user can add tasks, view the,l, mark them done, 
# and quit. Everything lives in a list while the program runs.
# ============================================================

# --- STEP 1: Create an empty list to store tasks ----
# A list holds multiple items in order, inside square brackets []
# Right now it's empty - tasks get added as the user runs the program

tasks = []

# --- STEP 2: Define functions ---

def show_menu():
    """ Prints the main menu options to the screen. """
    print("\n" + "=" * 40)
    print("         TO-DO LIST MENU")
    print("=" * 40)
    print("     1. View tasks")
    print("     2. Add a task ")
    print("     3. Mark a task as done")
    print("     4. Clear all tasks")
    print("     5. Quit")
    print("=" * 40)


def view_tasks():
    """ Displays all current tasks with a number next to each one."""
    if len(tasks) == 0:
        print("\nYour to-do list is empty. Add something!")
        return # return exits the function early - nothing left to do
    print(f"You have {len(tasks)} tasks(s) remaining.")

    # enumerate() gives you both the index AND the value as you loop
    # We start at 1 so the list shows 1, 2, 3 instead of 0, 1, 2
    for number, task in enumerate(tasks, start=1):
        print(f" {number}. {task}")

def add_task():
    """ Asks the user for a task and adds it to the list."""

    task = input("\nWhat task do you want to add? ").strip()
    # .strip() removes accidental spaces from the start and end

    if task in tasks:
        print("That task already exists!")
        return
    
    if task == "":
        print("You didn't type anything. Task not added.")
        return
    
    # .append() adds an item to the END of a list
    tasks.append(task)
    print(f"Added: '{task}'")


def complete_task():
    """ Lets the user pick a task to remove (mark as done)."""
    if choice < 1 or choice > len(tasks):
        print("That number is not on the list.")
        return 
    if len(tasks) == 0:
        print("\nNo tasks to complete. Add some first!")
        return
    
    
    view_tasks() 

    try:
        choice = int(input("\nEnter the number of the task you completed: "))

        if choice < 1 or choice > len(tasks):
       
         print("That number is not on the list.")

        
        finished = tasks[choice -1]

        tasks.remove(finished)

        print(f"Nice work! '{finished}' marked as done and removed.")

    except ValueError:
    
         print("Please enter a number, not text.")


print("=" * 40)
print(" Welcome to your Python To-Do list!")
print("=" * 40)

running = True

while running:
    show_menu()
    
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        tasks.clear()
        print("\nAll tasks cleared!")
    elif choice == "5":
        print("\nGood luck with your tasks. See you next time!")
        running = False
    else:
        print("Invalid option. Please choose 1, 2, 3, 4 or 5.")

    
