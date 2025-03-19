
from sqlalchemy import  ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

class User2(Base):
    __tablename__ = "users2"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_name= Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    bio= Column(String, nullable=True)
    profile_picture=Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Post2(Base):
    __tablename__ ="posts2"
    post_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users2.id", ondelete="CASCADE"), nullable=False)
    post = Column(String, nullable=False)
    media_type = Column(String, nullable=False)
    image_uri= Column(String, nullable=True)
    video_uri= Column(String, nullable=True)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
 
class Comments(Base):
    __tablename__ ="comments"
    comment_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users2.id", ondelete="CASCADE"), nullable=False)
    content_comment_id = Column(Integer, ForeignKey("contents.content_id", ondelete="CASCADE"), nullable=False)
    comment = Column(String, nullable=False)      
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #owner2 = relationship("User2")

class Likes(Base):
    __tablename__ ="likes"   
    user_id = Column(Integer, ForeignKey("users2.id", ondelete="CASCADE"), primary_key = True)
    content_like_id = Column(Integer, ForeignKey("contents.content_id", ondelete="CASCADE"), primary_key = True)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #owner3 = relationship("User2")

class DisLikes(Base):
    __tablename__ ="dislikes"
    user_id = Column(Integer, ForeignKey("users2.id", ondelete="CASCADE"), primary_key= True)
    content_dislike_id = Column(Integer, ForeignKey("contents.content_id", ondelete="CASCADE"), primary_key= True)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    #owner4 = relationship("User2")

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users2.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts2.post_id", ondelete="CASCADE"), primary_key=True)

class Contents(Base):
    __tablename__ ="contents"
    content_id = Column(Integer, primary_key=True, nullable=False)
    content_username = Column(String, nullable=True)
    content_user_picture = Column(String, nullable= True)
    media_type = Column(String, nullable=False)
    content_description = Column(String, nullable= True)
    image_title = Column(String, nullable=False)
    video_title = Column(String, nullable=False)
    video_url =Column(String, nullable=True)
    image_url = Column(String, nullable=True)    
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    images = Column(ARRAY(JSON), nullable=True)
    videos = Column(ARRAY(JSON), nullable=True)
    slider_images = Column(ARRAY(JSON), nullable=True)
    slider2_images = Column(ARRAY(JSON), nullable=True)
    slider2_videos = Column(ARRAY(JSON), nullable=True)
    

