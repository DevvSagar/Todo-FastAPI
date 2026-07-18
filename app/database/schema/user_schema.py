from sqlalchemy import Integer , DateTime , Boolean , String , VARCHAR 
from sqlalchemy.orm import Mapped , mapped_column
from ..db import Base
from datetime import datetime , timezone

class UserSchema(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer , primary_key=True , index=True , autoincrement=True)
    email: Mapped[str] = mapped_column(VARCHAR(255), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(VARCHAR(100) , nullable=False)
    password: Mapped[str] = mapped_column(String , nullable=False)
    confirm_password: Mapped[str] = mapped_column(String , nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean , default=True , nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at : Mapped[datetime] = mapped_column(DateTime,nullable=True,onupdate=lambda: datetime.now(timezone.utc))
