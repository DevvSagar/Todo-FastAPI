from fastapi import APIRouter , Depends , HTTPException
from app.models.todo import CreateTodo
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.database.schema import Todo_Schema 
from sqlalchemy import select 


router = APIRouter(prefix="/todo")

@router.get("/")
def index(db: Annotated[Session,Depends(get_db)]):
    stmt = select(Todo_Schema.id , Todo_Schema.content , Todo_Schema.is_completed)

    todos = db.execute(stmt).mappings().all()
    # todos = db.query(Todo_Schema).all()
    return{"Message": "This is todo Router", "Todo's": todos}

@router.get("/{id}")
def show(id: int , db: Annotated[Session , Depends(get_db)]):
    # stmt = select(Todo_Schema.id , Todo_Schema.content , Todo_Schema.is_completed).where(
    #     Todo_Schema.id == id
    # )
    todo = db.query(Todo_Schema).filter(Todo_Schema.id == id).first()
    return{
        "items": todo
    }



@router.post("/")
def store(todo_item:CreateTodo , db: Annotated[Session,Depends(get_db)]):
    todo = Todo_Schema(content = todo_item.content , is_completed = todo_item.is_completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "Message" : "Todo items", 
           "item": todo
    }

@router.put("/{id}")
def update(id: int, add_item:CreateTodo, db:Annotated[Session , Depends(get_db)]):
    todo = db.query(Todo_Schema).filter(Todo_Schema.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found !!!")
    
    todo.content = add_item.content
    todo.is_completed = add_item.is_completed
    db.commit()
    db.refresh(todo)
    return{"Message": "Todo item Updated", "update": todo}

@router.delete("/{id}")
def delete(id: int , db : Annotated[Session , Depends(get_db)]):
    todo = db.query(Todo_Schema).filter(Todo_Schema.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found !!!")
    
    db.delete(todo)
    db.commit()
    return{"Message": "Todo Deleted"}