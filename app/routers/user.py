from typing import List
from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from random import randrange
from psycopg2.extras import RealDictCursor
from .. import models, schemas, utils, oauth2
from .. database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/users", tags=['User'], redirect_slashes=False)

@router.get("/", response_model=List[schemas.UserResponse])
def get_users( db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    
    return users

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user {id} was not found")
    return user

@router.put("/{id}")
def update_user(user: schemas.UserCreate, id: int, db:Session = Depends(get_db), 
                current_user: int = Depends(oauth2.get_current_user)
                 ):
    hash_password = utils.hash(user.password)
    user.password = hash_password

    user_query = db.query(models.User).filter(models.User.id==id)
    updated_user = user_query.first()
    print(current_user.id)
    if updated_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post {id} not found")
    if id != current_user:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized")
    
    user_query.update(user.model_dump(), synchronize_session=False)
    db.commit() 
    db.refresh(user_query.first())     
    return user_query.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db:Session = Depends(get_db), 
                current_user: int = Depends(oauth2.get_current_user)):

    user_query = db.query(models.User).filter(models.User.id==id)
    deleted_user = user_query.first()
    
    if deleted_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post {id} not found")
    if id != current_user.id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized")

    user_query.delete(synchronize_session=False)
    print(current_user.id)
    db.commit()
    #db.refresh()
    return Response(status_code=status.HTTP_204_NO_CONTENT)