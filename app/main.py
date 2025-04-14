import uvicorn
from typing import List
from fastapi import FastAPI, HTTPException, status, Response, Depends
from random import randrange
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from . database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote, content, likes, login, users2, comments, dislikes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


#models.Base.metadata.create_all(bind=engine)

app= FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,     
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

@app.get("/")
def root():
    return {"message": "Welcome to RestApi Project"}

@app.get("/sqlalchemy", response_model=List[schemas.PostCreate])
def test_post(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
       
    return posts

app.include_router(post.router)
#app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(content.router)
app.include_router(likes.router)
app.include_router(users2.router)
app.include_router(login.router)
app.include_router(comments.router)
app.include_router(dislikes.router)

#if __name__ == '__main__':
    #uvicorn.run('app.main:app', 
                #host= "0.0.0.0",
                #port = 8080,
                #log_level = "debug",
                #reload = True)

