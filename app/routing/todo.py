from fastapi import APIRouter , Depends
from app.models.todo import CreateTodo


router = APIRouter(prefix="/todo")

@router.get("/")
def index():
    return{"Message": "This is todo Router"}

@router.post("/")
def store(todo:CreateTodo):
    return{
        "Message" : "Todo items", 
           "item": todo.model_dump()
    }