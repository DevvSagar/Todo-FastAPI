from fastapi import APIRouter , Depends , HTTPException
from app.schema.todo import CreateTodo
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.todo import TodoModel 
from sqlalchemy import select 
from app.dependencies import authenicate_user
from app.models.user import UserModel


router = APIRouter(prefix="/todo" , dependencies=[Depends(authenicate_user)])



@router.get("/")
def index(db: Annotated[Session,Depends(get_db)], current_user: Annotated[dict, Depends(authenicate_user)]):

    user = db.query(UserModel).filter(UserModel.email == current_user["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    stmt = select(TodoModel.id , TodoModel.content , TodoModel.is_completed).filter(TodoModel.user_id == user.id)

    todos = db.execute(stmt).mappings().all()
    # todos = db.query(TodoModel).all()
    return{"Message": "This is todo Router", "Todo's": todos}





@router.get("/{id}")
def show(id: int, db: Annotated[Session, Depends(get_db)] , current_user: Annotated[dict, Depends(authenicate_user)]):
    user = db.query(UserModel).filter(UserModel.email == current_user["sub"]).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    todo = db.query(TodoModel).filter(TodoModel.user_id == user.id).filter(TodoModel.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found !!!")
    return {"items": todo}






@router.post("/")
def store(todo_item:CreateTodo , db: Annotated[Session,Depends(get_db)] , current_user: Annotated[dict, Depends(authenicate_user)]):
    user = db.query(UserModel).filter(UserModel.email == current_user["sub"]).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    todo = TodoModel(
        content=todo_item.content,
        is_completed=todo_item.is_completed,
        user_id=user.id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "Message" : "Todo items", 
           "item": todo
    }





@router.put("/{id}")
def update(id: int, add_item:CreateTodo, db:Annotated[Session , Depends(get_db)] , current_user: Annotated[dict, Depends(authenicate_user)]):

    user = db.query(UserModel).filter(UserModel.email == current_user["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")


    todo = db.query(TodoModel).filter(TodoModel.user_id == user.id).filter(TodoModel.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found !!!")
    
    todo.content = add_item.content
    todo.is_completed = add_item.is_completed
    db.commit()
    db.refresh(todo)
    return{"Message": "Todo item Updated", "update": todo}






@router.delete("/{id}")
def delete(id: int , db : Annotated[Session , Depends(get_db)] , current_user: Annotated[dict, Depends(authenicate_user)]):
    user = db.query(UserModel).filter(UserModel.email == current_user["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    todo = db.query(TodoModel).filter(TodoModel.user_id == user.id).filter(TodoModel.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Item not found !!!")
    
    db.delete(todo)
    db.commit()
    return{"Message": "Todo Deleted"}