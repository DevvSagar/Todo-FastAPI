from fastapi import APIRouter , Depends
from app.models.todo import CreateTodo
from typing import Annotated


router = APIRouter(prefix="/todo")

@router.get("/")
def index():
    return{"Message": "This is todo Router"}

@router.post("/")
def store(app:CreateTodo):
    return{
        "Message" : "Todo items", 
           "item": app.model_dump()
    }