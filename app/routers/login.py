from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, models,utils, oauth_user2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

@router.post('/login2', response_model=schemas.TokenUser2)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User2).filter(models.User2.email == user_credentials.username).first()

    if not user: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid Credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    access_token = oauth_user2.create_access_token(data={"user_id": user.id})

    return {"access_token":access_token, "token_type": "bearer", "user": user}