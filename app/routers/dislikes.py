from typing import List
from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from random import randrange
from psycopg2.extras import RealDictCursor
from sqlalchemy import func
from .. import models, schemas, utils, oauth_user2
from .. database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/dislikes", tags=['DisLikes'], redirect_slashes=False)

@router.get("/", response_model= List[schemas.DisLikesResponse])
            
def get_dislikes( db:Session = Depends(get_db)):
    dislike = db.query(models.User2.id, models.User2.email, models.DisLikes.content_dislike_id).join(models.DisLikes, models.User2.id==models.DisLikes.user_id, isouter=False).all()
    print(dislike)    
    return dislike

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_dislike(dislike:schemas.DisLikes, db:Session = Depends(get_db), current_user: int = Depends(oauth_user2.get_current_user)):    
    
    #like = db.query(models.Contents4).filter(models.Contents4.content_id == like.content_like_id).first()
    #if not like: 
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Like {like.content_id} not found")

    dislike_query = db.query(models.DisLikes).filter(models.DisLikes.content_dislike_id==dislike.content_dislike_id, models.DisLikes.user_id==current_user.id)
    found_like = dislike_query.first()
    if(dislike.dir == 1):
        if(found_like):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user{current_user.id} has voted already')
        new_like = models.DisLikes(content_dislike_id = dislike.content_dislike_id, user_id = current_user.id)
        db.add(new_like)
        db.commit()
        return {"msg": "content successfully disliked"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No likes found")

        dislike_query.delete(synchronize_session=False)
        db.commit()
        return {"msg": "like successfully deleted"}
    