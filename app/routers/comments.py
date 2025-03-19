from typing import List
from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from random import randrange
from psycopg2.extras import RealDictCursor
from .. import models, schemas, utils, oauth_user2
from .. database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/comments", tags=['Comments'], redirect_slashes=False)

@router.get("/", response_model=List[schemas.CommentResponse3])
def get_comments( db:Session = Depends(get_db)):
    comments = db.query(models.User2.first_name, models.User2.last_name, models.User2.user_name,models.User2.bio,models.User2.profile_picture, 
                        models.Comments.comment_id,models.Comments.user_id,models.Comments.content_comment_id,models.Comments.comment,models.Comments.created_at).join(models.Comments, models.User2.id==models.Comments.user_id, isouter=False).all()
    print(comments)
    return comments

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Comments)
def create_comment(comment:schemas.CommentRequest, db:Session = Depends(get_db), current_user: int = 
                 Depends(oauth_user2.get_current_user)):
    comment_query = db.query(models.Comments).filter(models.Comments.user_id == current_user.id)
    user = comment_query.first()
    print(type(user))
    #print(current_user.id)
    print(user)
    #if user.user_id != current_user.id:
        #raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    #user = current_user    
    new_comment = models.Comments(**comment.model_dump())
    print(new_comment)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/{id}", response_model=schemas.Comments)
def get_comment(id: int, db:Session = Depends(get_db)):
    comment = db.query(models.Comments).filter(models.Comments.comment_id == id).first()
    
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user {id} was not found")
    return comment

@router.put("/{id}")
def update_comment(comment: schemas.CommentRequest, id: int, db:Session = Depends(get_db), 
                current_user: int = Depends(oauth_user2.get_current_user)):
    
    comment_query = db.query(models.Comments).filter(models.Comments.comment_id==id)
    updated_comment = comment_query.first()
    print(updated_comment.user_id)
    print(current_user.id)
    if updated_comment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post {id} not found")
    if updated_comment.user_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized")
    
    comment_query.update(comment.model_dump(), synchronize_session=False)
    db.commit() 
    db.refresh(comment_query.first())     
    return comment_query.first()

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(id: int, db:Session = Depends(get_db), 
                current_user: int = Depends(oauth_user2.get_current_user)):

    comment_query = db.query(models.Comments).filter(models.Comments.comment_id==id)
    deleted_comment = comment_query.first()
    
    if deleted_comment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post {id} not found")
    if deleted_comment.user_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized")

    comment_query.delete(synchronize_session=False)
    print(current_user.id)
    db.commit()
    #db.refresh()
    return Response(status_code=status.HTTP_204_NO_CONTENT)