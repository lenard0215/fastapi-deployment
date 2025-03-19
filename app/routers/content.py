from typing import List, Optional
from fastapi import HTTPException, status, Response, Depends, APIRouter
from .. import models, schemas, oauth2
from .. database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/content", tags=['Content2'])

@router.get("/",response_model= List[schemas.Content])
def get_content(db:Session = Depends(get_db), limit:str = 100, search:Optional[str] = "" ):
    content = db.query(models.Contents).filter(models.Contents.content_user_picture.contains(search)).limit(limit).all()
    
    return content