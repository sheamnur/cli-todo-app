class Task():
    tasks={}
    def add_task(self,task_name,id):
        self.tasks[id]={
            "title": task_name,
            "status":"Incomplete"
        }
        print("Task added successfully.")
    def show_all_task(self):
        for key,value in self.tasks.items():
            print(key,value)
    
    def search_task(self,id):
        if id in self.tasks:
            print("Task is found.")
            print(f"Task id={id}")
            print(f"Task title={self.tasks[id]['title']}")
            print(f"Task status={self.tasks[id]['status']}")
            return
        print("Task is not found.")
    
                
    def complete_task(self,id):
        if id in self.tasks:
            if self.tasks[id]['status']=="Complete":
                print("Task already Completed!")
                return
            self.tasks[id]['status']="Complete"
            print("Task completed now.")
            return
        print("Task is not found.")

    def update_task(self,id):
        if id in self.tasks:
            while True:

                task_name=input("Enter the update task title: ")
                if task_name.isdigit() or task_name.isspace() or task_name=="":
                    print("Task name cannot be just integer or empty.")
                else:
                    break

            status=input("Enter the task status: ")
            while  status not in ["Complete","Incomplete"]:
                print("Please enter either 'Complete' or 'Incomplete'")
                status=input("Enter status for the task again: ")

            self.tasks[id]['title']=task_name
            self.tasks[id]['status']=status
            print("Task updated successfully.")
            return
    
                
        print("Task is not found.")

    def delete_task(self,id):
        if id in self.tasks:
            del self.tasks[id]
            print("Task deleted successfully.")
            return
        else:
            print("Task not found.")
    
    