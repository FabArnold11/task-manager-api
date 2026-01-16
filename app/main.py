from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.session import engine, get_db
from app.db.base import Base
from app.models import user
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user

app = FastAPI(title="Task Manager API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "API running"}

@app.post("/users", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


