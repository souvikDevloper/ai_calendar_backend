from sqlalchemy import Column, Integer, String
from services.database import Base
from pydantic import BaseModel, EmailStr
import bcrypt

# ✅ User Table (SQLAlchemy Model)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # ✅ Password Hashing Function
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # ✅ Password Verification Function
    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())

# ✅ Pydantic Schema for User Registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# ✅ Pydantic Schema for User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
