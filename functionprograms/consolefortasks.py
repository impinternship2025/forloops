# Get no of tasks
# Loop through tasks
# 

# Push to a list of dicts

# Enter options 

tasks = []

def get_task_information():
    description = input("Enter task description: ")
    while description == "" or description.isdigit():
        description = input("Invalid. Description cannot be empty or a number: ")

    categories = ["HR", "Finance", "Development"]
    print("Available categories: HR, Finance, Development")
    category = input("Enter category: ")
    while category != "HR" and category != "Finance" and category != "Development":
        print("Invalid category. Please choose from HR, Finance, Development.")
        category = input("Enter category: ")

    time = input("Enter estimated time (hours): ")
    while not time.isdigit() or int(time) <= 0:
        time = input("Invalid. Enter a positive number: ")
    time = int(time)

    print("Status options: Not Started, In Progress, Completed")
    status = input("Enter status: ")
    while status != "Not Started" and status != "In Progress" and status != "Completed":
        status = input("Invalid. Enter status as exactly: Not Started, In Progress, or Completed: ")

    task = {
        "description": description,
        "category": category,
        "estimated_time": time,
        "status": status
    }

    tasks.append(task)
    print(" Task added!\n")
    start()

def display_all_tasks():
    if not tasks:
        print("\nNo tasks added yet.")
    else:
        print("\nAll Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']} | {task['category']} | {task['estimated_time']} hrs | {task['status']}")
    start()

def display_tasks_to_be_done_today():
    print("\nTasks to be completed today:")
    found = False
    for task in tasks:
        if task["status"] != "Completed":
            print(f"- {task['description']} [{task['status']}]")
            found = True
    if not found:
        print("All tasks completed!")
    start()

def display_tasks_not_started():
    print("\nTasks Not Started:")
    found = False
    for task in tasks:
        if task["status"] == "Not Started":
            print(f"- {task['description']}")
            found = True
    if not found:
        print("No tasks are in 'Not Started' status.")
    start()

def display_completed_task_count():
    completed = [task for task in tasks if task["status"] == "Completed"]
    print(f"\n You have completed {len(completed)} task(s).")
    start()

def choose_option():
    options = """\n========= Task Manager =========
1 - Add a task
2 - View all tasks
3 - View tasks to be done today
4 - View not started tasks
5 - View number of completed tasks
6 - Exit
"""
    return input(options)

def go_to_option(option):
    if option == "1":
        get_task_information()
    elif option == "2":
        display_all_tasks()
    elif option == "3":
        display_tasks_to_be_done_today()
    elif option == "4":
        display_tasks_not_started()
    elif option == "5":
        display_completed_task_count()
    elif option == "6":
        print("Exiting. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
        start()

def start():
    selected_option = choose_option()
    go_to_option(selected_option)


start()
