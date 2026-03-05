tasks = []

def display_tasks():
    if not tasks:
        print("No tasks yet.")

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
