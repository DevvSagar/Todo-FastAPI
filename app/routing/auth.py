from fastapi import APIRouter , Depends
from app.database.db import get_db
from sqlalchemy.orm import Session
from app.models.user import Register , Login
from typing import Annotated





router = APIRouter(prefix="/auth")

@router.post("/register")
def register(data:register , db: Annotated[Session , Depends(get_db)]):
    

