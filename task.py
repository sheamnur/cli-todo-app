class Task():
    tasks={}
    def add_task(self,task_name,id):
        self.task_name=task_name
        self.id=id
        self.tasks[id]={
            "title": task_name,
            "status":"incomplete"
        }
        print("Task add successfully.")
    def show_all_task(self):
        for key,value in self.tasks.items():
            print(key,value)
    
    def search_task(self,id):
        for key,value in self.tasks.items():
            if key==id:
                print("Task is found.")
                print(f"Task ={value}")
                return
        print("Task is not found.")
    
                
    def complete_task(self,id):
        for key,value in self.tasks.items():
            if key==id:
                self.tasks[key]["status"]="complete"
                print("Task is complete now.")
                return
        print("Task is not found.")

    def update_task(self,id):
        for key,value in self.tasks.items():
            if key==id:
                task_name=input("Enter the update task: ")
                status=input("Enter status for the task: ")
                self.tasks[key]["title"]=task_name
                self.tasks[key]["status"]=status
                return
        print("Task is not found.")

    def delete_task(self,id):
        if id in self.tasks:
            del self.tasks[id]
            return
        else:
            print("Task not found.")
    
    