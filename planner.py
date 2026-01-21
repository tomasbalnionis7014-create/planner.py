# with this we can practice loops, conditionals, inputs, outputs and operators

tasks = []
while True:
    options = ["1) view tasks", "2) add tasks", "3) remove tasks", "4) exit"]
    print("Please choose an option:")
    for option in options:
        print(option)
    choice = input("Enter the number of your choice: ")
    if choice == "4":
        print("The planner shall now terminate MWAHAHAHHA")
        break
    elif choice == "1":
        print("Your tasks for today are:")
        print(tasks)
    elif choice == "2":
        task_for_today = input("What must be done today? ")
        if task_for_today == "":
            print("You must enter a task to add it to your planner.")
        elif task_for_today.lower() not in tasks:
            tasks.append(task_for_today.lower())
            print(f"Task '{task_for_today}' added to your planner.")
        elif task_for_today.lower() in tasks:
            print(f"Task '{task_for_today}' is already in your planner.")
    elif choice == "3":
        remove_this_task = input(
            "human being, which task do you want to remove? ")
        if remove_this_task.lower() in tasks:
            tasks.remove(remove_this_task.lower())
            print(f"This task: '{remove_this_task}' has now been removed.")
        elif remove_this_task.lower() not in tasks:
            print(f"This task: '{remove_this_task}' is not in your planner.")
        print(f"Your remaining tasks are:'{tasks}'")
        print("Make sure to do them you human being")
