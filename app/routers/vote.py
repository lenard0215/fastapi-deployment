from fastapi import HTTPException, status, Response, Depends, APIRouter
from .. import schemas, oauth2, models
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/vote", tags=["Vote"])

@router.post("/", status_code=status.HTTP_201_CREATED)

def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = 
                 Depends(oauth2.get_current_user)):
    vote_query =db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if (vote.dir ==1):
        
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail=f"you have already voted")
        new_vote = models.Vote(post_id = vote.post_id, user_id= current_user.id)
        db.add(new_vote)
        db.commit()
        return {"msg": "vote successful"}

    else: 
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}
