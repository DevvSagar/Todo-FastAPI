from sqlalchemy import Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import Mapped , mapped_column
from ..database.db import Base
from datetime import datetime, timezone

class TodoModel(Base):
    __tablename__ = "todos"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    content : Mapped[str] = mapped_column(String, nullable=False)
    is_completed : Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at : Mapped[datetime] = mapped_column(DateTime,nullable=True,onupdate=lambda: datetime.now(timezone.utc))
    


