"""
1. Add Task
2. Show Tasks
3. Delete Task
4. Complete Task
5. Update Task
6. Exit
"""
from task import Task
from storage import Storage
storage=Storage()
task=Task()
Task.tasks=storage.load_task()
print("==========CLI TODO APP========")
print("1. Add Task")
print("2. Show Task")
print("3. Search Task")
print("4. Delete Task")
print("5. Complete Task")
print("6. Update Task")
print("7. Exit")

while True:
    choice=input("Enter your choice: ")
    if choice=='1':
        print("----Add Task----")
        while True:
            try:
                task_id=int(input("Enter task id: "))
                if task_id in Task.tasks:
                    print("Task id already exist!")
                    continue
                break
            except ValueError:
                print("Task id can only be integer.")
        while True:
            task_name=input("Enter task title: ")
            if task_name.isdigit() or task_name.isspace() or task_name=="":
                print("Task name cannot be just integer or empty.")
            else:
                break
        task.add_task(task_name,task_id)
        storage.save_task(Task.tasks)
    elif choice=='2':
        print("----All Task----")
        task.show_all_task()
    elif choice=='3':
        print("----Search Task----")
        while True:
            try:
                task_id=int(input("Enter task id: "))
                break
            except ValueError:
                print("Enter valid task id(integer).")
        task.search_task(task_id)
    elif choice=='4':
        print("----Delete Task----")
        while True:
            try:
                task_id=int(input("Enter task id: "))
                break
            except ValueError:
                print("Enter valid task id(integer).")
        task.delete_task(task_id)
        storage.save_task(Task.tasks)
    elif choice=='5':
        print("----Complete Task----")
        while True:
            try:
                task_id=int(input("Enter task id: "))
                break
            except ValueError:
                print("Enter valid task id(integer).")
        task.complete_task(task_id)
        storage.save_task(Task.tasks)
    elif choice=='6':
        print("----Update Task----")
        while True:
            try:
                task_id=int(input("Enter task id: "))
                break
            except ValueError:
                print("Enter valid task id(integer).")
        task.update_task(task_id)
        storage.save_task(Task.tasks)
    elif choice=='7':
        print("Have a good day.Bye.")
        break
    else:
        print("Invalid choice!")

