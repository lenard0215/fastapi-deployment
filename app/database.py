from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

ENV = 'Dev'
if ENV == 'Dev':
    #SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:AuriJoe0215@localhost/retrofitapp'
    SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
else:
    SQLALCHEMY_DATABASE_URL = f'postgresl://u1i4dqsvo8mmi9:pd1314b726da00b1b1386f7523216c8225111d31d169832da479ab11904bf3510@ce0lkuo944ch99.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d31tfvv5qkvpst?sslmode=require'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#while True:
    #try:
        #conn=psycopg2.connect(host= 'localhost', database='retrofitapp', user='postgres', 
                              #password = 'AuriJoe0215', cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print("Database connection successful!!")
        #break
    #except Exception as error:
        #print("Connecting to database failed")
        #print("Error:", error)
        #time.sleep(2)