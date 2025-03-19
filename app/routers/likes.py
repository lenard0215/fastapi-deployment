from typing import List
from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from random import randrange
from psycopg2.extras import RealDictCursor
from sqlalchemy import func
from .. import models, schemas, utils, oauth_user2
from .. database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/likes", tags=['Likes'], redirect_slashes=False)

@router.get("/", response_model= List[schemas.LikesResponse])            
def get_likes( db:Session = Depends(get_db)):
    like = db.query(models.User2.id, models.User2.email, models.Likes.content_like_id).join(models.Likes, models.User2.id==models.Likes.user_id, isouter=False).all()
    print(like)    
    return like

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_like(like:schemas.Likes, db:Session = Depends(get_db), current_user: int = Depends(oauth_user2.get_current_user)):    
    
    #like = db.query(models.Contents4).filter(models.Contents4.content_id == like.content_like_id).first()
    #if not like: 
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Like {like.content_id} not found")

    like_query = db.query(models.Likes).filter(models.Likes.content_like_id==like.content_like_id, models.Likes.user_id==current_user.id)
    found_like = like_query.first()
    #print(current_user.id)
    if(like.dir == 1):
        if(found_like):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user{current_user.id} has voted already')
        new_like = models.Likes(content_like_id = like.content_like_id, user_id = current_user.id)
        db.add(new_like)
        db.commit()
        return {"msg": "content successfully liked"}
    else:
        #if not found_like:
            #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No likes found")

        like_query.delete(synchronize_session=False)
        db.commit()
        return {"msg": "like successfully deleted"}
    