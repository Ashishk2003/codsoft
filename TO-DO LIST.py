import json
import os

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks.append({"title": title, "description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx}. {task['title']} - {status}")
        print(f"   Description: {task['description']}")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to update: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            print(f"Updating task '{task['title']}':")
            new_title = input("Enter new title (leave blank to keep current): ").strip()
            new_description = input("Enter new description (leave blank to keep current): ").strip()
            if new_title:
                task["title"] = new_title
            if new_description:
                task["description"] = new_description
            save_tasks(tasks)
            print(f"Task '{task['title']}' updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_number - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
