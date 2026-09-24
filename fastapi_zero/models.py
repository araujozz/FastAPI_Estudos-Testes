from sqlalchemy.orm import Mapped
from datetime import datetime

class User:
    __tablename__ = 'users'
    
    id: Mapped[int]
    usuario: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    created_at: Mapped[datetime]