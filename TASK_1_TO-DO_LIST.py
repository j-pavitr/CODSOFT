Mfile = "List.txt"

def load():
    try:
        with open(Mfile, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save(tasks):
    with open(Mfile, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add():
    task = input("Enter task: ")
    tasks = load()
    tasks.append("[ ] " + task)
    save(tasks)
    print(" Task added.")

def done():
    tasks = load()
    if not tasks:
        print(" No tasks!")
        return

    print(" Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    index = int(input("Task number to mark as done: "))
    if 0 < index <= len(tasks):
        tasks[index - 1] = tasks[index - 1].replace("[ ]", "[<>]", 1)
        save(tasks)
        print(" Task marked as done.")
    else:
        print(" Invalid number.")

def delete():
    tasks = load()
    if not tasks:
        print(" No tasks!")
        return

    print(" Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    index = int(input("Task number to remove: "))
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save(tasks)
        print(f" Removed: {removed}")
    else:
        print(" Invalid number.")

def show():
    tasks = load()
    if not tasks:
        print(" No tasks!")
    else:
        print(" Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def menu():
    while True:
        print("\n TO-DO LIST MENU")
        print("1. Show All")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show()
        elif choice == "2":
            add()
        elif choice == "3":
            done()
        elif choice == "4":
            delete()
        elif choice == "5":
            print(" Bye!")
            break
        else:
            print(" Invalid choice. Try again.")

menu()
