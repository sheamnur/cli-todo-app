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
print("3. Delete Task")
print("4. Complete Task")
print("5. Update Task")
print("6. Exit")

while True:
    choice=input("Enter your choice: ")
    if choice=='1':
        task_name=input("Enter task title: ")
        task_id=int(input("Enter task id: "))
        task.add_task(task_name,task_id)
        storage.save_task(Task.tasks)
    elif choice=='2':
        try:
            task.show_all_task()
        except:
            print("No task add yet.")
    elif choice=='3':
        task_id=int(input("Enter task id: "))
        task.delete_task(task_id)
        storage.save_task(Task.tasks)
    elif choice=='4':
        task_id=int(input("Enter task id: "))
        task.complete_task(task_id)
        storage.save_task(Task.tasks)
    elif choice=='5':
        task_id=int(input("Enter task id: "))
        task.update_task(task_id)
        storage.save_task(Task.tasks)
    elif choice=='6':
        break
    else:
        print("Invalid choice!")

