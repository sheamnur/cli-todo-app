class Storage:
    def save_task(self,tasks):
        with open("task.txt",'w') as file:
            for task_id,task in tasks.items():
                file.write(f"{task_id},{task['title']},{task['status']}\n")

    def load_task(self):
        tasks={}
        try:
            with open("task.txt",'r') as file:
                for line in file:
                    data=line.strip().split(",")
                    task_id=data[0]
                    task_name=data[1]
                    task_status=data[2]
                    tasks[int(task_id)]={
                        "title":task_name,
                        "status":task_status
                    }
        except FileNotFoundError:
            pass
        return tasks


