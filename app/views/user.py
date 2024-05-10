from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from app.config.database import get_db
from app.models import User
from app.serializers import CreateUserSerializer, RetrieveUserSerializer, ListUserSerializer

def create_user(user: CreateUserSerializer, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail=f"User with that {user.email} already exists")
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    return RetrieveUserSerializer.model_validate(new_user)

def list_user(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return ListUserSerializer.model_validate({'users':users})

def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return RetrieveUserSerializer.model_validate(user)

def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # update
    db.query(User).filter(User.id == user_id).update(user_data)
    db.commit()
    return RetrieveUserSerializer.model_validate(user)
    

def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()