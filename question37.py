# Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.
tasks = []

while True:
    print("\n------ TO-DO LIST MANAGER ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")


    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

  
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to remove: "))
            
            if num >= 1 and num <= len(tasks):
                removed_task = tasks.pop(num - 1)
                print("Removed task:", removed_task)
            else:
                print("Invalid task number.")

  
    elif choice == '4':
        print("Exiting To-Do List Manager...")
        break

    else:
        print("Invalid choice! Try again.")

        # . Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing 
# tasks  

