from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter()

tasks_db = []

# ✅ CREATE TASK (INPUT BOX WILL COME HERE)
@router.post("/", response_model=TaskResponse)
def add_task(task: TaskCreate):
    new_task = {
        "id": len(tasks_db) + 1,
        "title": task.title,
        "description": task.description
    }
    tasks_db.append(new_task)
    return new_task


# ✅ GET TASKS (NO INPUT BOX - THIS IS CORRECT)
@router.get("/", response_model=List[TaskResponse])
def list_tasks():
    return tasks_db