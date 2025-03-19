from typing import List
from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from random import randrange
from psycopg2.extras import RealDictCursor
from .. import models, schemas, utils, oauth_user2
from .. database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/users2", tags=['User2'], redirect_slashes=False)

@router.get("/", response_model=List[schemas.UserResponse2])
def get_users( db:Session = Depends(get_db),current_user: int = 
                 Depends(oauth_user2.get_current_user)):
    users = db.query(models.User2).all()
    
    return users

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse2)
def create_user(user:schemas.User2Request, db:Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User2(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserResponse2)
def get_user(id: int, db:Session = Depends(get_db),current_user: int = 
                 Depends(oauth_user2.get_current_user)):
    user = db.query(models.User2).filter(models.User2.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user {id} was not found")
    return user

@router.put("/{id}")
def update_user(user: schemas.User2Request, id: int, db:Session = Depends(get_db), 
                current_user: int = Depends(oauth_user2.get_current_user)):
    hash_password = utils.hash(user.password)
    user.password = hash_password

    user_query = db.query(models.User2).filter(models.User2.id==id)
    updated_user = user_query.first()

    if updated_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post {id} not found")
    if id != current_user.id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized")
    
    user_query.update(user.model_dump(), synchronize_session=False)
    db.commit() 
    db.refresh(user_query.first())     
    return user_query.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db:Session = Depends(get_db), 
                current_user: int = Depends(oauth_user2.get_current_user)):

    user_query = db.query(models.User2).filter(models.User2.id==id)
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