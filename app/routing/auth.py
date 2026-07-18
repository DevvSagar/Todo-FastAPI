from fastapi import APIRouter , Depends , HTTPException
from app.models.user import Register , Login
from app.database.db import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from app.database.schema import UserSchema
from fastapi.responses import JSONResponse
from app.helper import hashpassword , verifyPassword , create_access_token , verify_token

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(data: Login , db:Annotated[Session , Depends(get_db)]):
    user = db.query(UserSchema).filter(UserSchema.email == data.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid User")
    
    if not verifyPassword(data.password , user.password):
        raise HTTPException(status_code=401, detail="Invalid Password")
    
    payload = {

    }
    
    return {
        "Message" : "Logged In !!",
        "user": user
    }



@router.post("/register")
def register(data: Register , db:Annotated[Session , Depends(get_db)]):
    existing_user = db.query(UserSchema).filter(UserSchema.email == data.email).first()
    if existing_user:
        return JSONResponse({"Message" : "User exists with the Email !!!!"}, status_code= 400)
    
    # Creating New user

    new_user = UserSchema(
        name = data.name,
        email = data.email,
        password = hashpassword(data.password),
        confirm_password = hashpassword(data.confirm_password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "Message": "User is Created Successfully !!!j",
        "item" : new_user
    }
    


