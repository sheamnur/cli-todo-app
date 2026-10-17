from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import Database
from task import Task
app=FastAPI()
database=Database()
class Tasks(BaseModel):
    title:str

@app.get("/tasks",status_code=200)
def show_tasks():
    tasks=database.get_task()
    if tasks is None:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )
    return tasks


@app.post("/tasks",status_code=201)
def add_tasks(task:Tasks):
    title=task.title
    task=Task(title)
    result=database.add_task(task)
    if result:
        return{"message":"Task add successfully."}
    else:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )

@app.patch("/tasks/{task_id}")
def update_task(task_id:int,task:Tasks):
    title=task.title
    result=database.update_task(task_id,title)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )
    if result:
        return{"message":"Task update successfully."}
    else:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    result=database.delete_task(task_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )
    if result:
        return{"message":"Task deleted successfully."}
    else:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )
@app.patch("/tasks/{task_id}/status")
def complete_task(task_id:int):
    result=database.complete_tasks(task_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found."
        )
    if result:
        return{"message":"Task mark as complete."}
    else:
        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )
    
    
        
