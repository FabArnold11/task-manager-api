from pydantic import BaseModel, EmailStr

# Schema para criar usuário
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema para leitura de usuário
class UserRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # Substitui orm_mode