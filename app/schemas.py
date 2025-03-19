from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime



class PostBase(BaseModel):
    title:str
    content:str
    #published: bool

class PostCreate(PostBase):
    pass

class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    #created_at: datetime
    class Config:
        orm_mode =True

class User2(BaseModel):
    id : int 
    first_name : str
    last_name : str
    user_name : str
    email : str
    password : str
    bio : str
    profile_picture : str
    created_at : datetime 
    class Config:
        orm_mode =True

class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: User    
    class Config:
        orm_mode =True

class Post2(BaseModel):
    post_id : int
    user_id : int
    post : str
    media_type : str
    image_uri : str
    video_uri : str
    published : bool
    created_at : datetime
    class Config:
        orm_mode =True

class PostCreate2(BaseModel):
    post : str
    media_type : str
    image_uri : str
    video_uri : str
    

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse2(BaseModel):
    id: int
    first_name : str
    last_name : str
    user_name : str
    email : str
    bio : str
    profile_picture : str    
    created_at: datetime

class UserResponse3(BaseModel):
    #id: int
    first_name : str
    last_name : str
    user_name : str
    bio : str
    profile_picture : str    
    class Config:
        orm_mode =True

class User2Request(BaseModel):    
    first_name : str
    last_name : str
    user_name : str
    email : str
    password : str
    bio : str
    profile_picture : str
    
class UserResponse(BaseModel):
    email: EmailStr
    id: int    

class Userlogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenUser2(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse2

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint

class Content(BaseModel):
    content_id : int
    content_username: str
    content_user_picture: str
    media_type : str
    content_description : str
    image_title : str
    video_title : str
    video_url : str
    image_url : str    
    created_at : datetime
    images : list[object]
    videos : list[object]
    slider_images : list[object]
    slider2_images :list[object]
    slider2_videos :list[object]
    class Config:
        orm_mode =True   

class Content2(BaseModel):
    content_id : int
    media_type : str
    image_title : str
    video_title : str
    video_url : str
    image_url : str    
    created_at : datetime
    images_url : list[str]
    images_titles : list[str]
    videos_url : list[str]
    videos_titles : list[str]
    slider_images : list[str]
    slider_images_titles : list[str]
    slider2_images : list[str]
    slider2_images_titles : list[str]
    slider2_videos : list[str]
    slider2_videos_titles : list[str]
    class Config:
        orm_mode =True

    
class Content3(BaseModel):   
    content_id : int
    media_type : str
    image_title : str
    video_title : str
    video_url : str
    image_url : str    
    created_at : datetime
    images : object
    videos : object
    slider_images : object
    slider2_images : object
    slider2_videos : object
    class Config:
        orm_mode =True

class Content4(BaseModel):   
    content_id : int
    media_type : str
    image_title : str
    video_title : str
    video_url : str
    image_url : str    
    created_at : datetime
    images : list[object]
    videos : list[object]
    slider_images : list[object]
    slider2_images :list[object]
    slider2_videos :list[object]
    class Config:
        orm_mode =True

class CommentRequest(BaseModel):    
    user_id : int
    content_comment_id : int
    comment : str          

class Comments(BaseModel):
    comment_id : int
    user_id : int
    content_comment_id : int
    comment : str      
    published : bool
    created_at : datetime  

class CommentResponse(BaseModel):
    content_comment_id: int
    created_at : str
    published : bool
    comment : str
    comment_id : int    
    user_id : int
    

class CommentResponse2(BaseModel):    
    id: int
    first_name : str
    last_name : str
    user_name : str
    email : EmailStr
    password: str
    bio : str
    profile_picture : str    
    created_at: datetime
    comment_id : int
    user_id : int
    content_comment_id : int
    comment : str      
    published : bool
    created_at : datetime 
    class Config:
        orm_mode =True
    
class CommentResponse3(BaseModel): 
    first_name : str
    last_name : str
    user_name : str
    bio : str
    profile_picture : str
    comment_id : int
    user_id : int
    content_comment_id : int
    comment : str      
    #published : bool
    created_at : datetime 

class ContentJoin(Content):
    Content: Content
    image: list
    title: list
    class Config:
        orm_mode =True

class Likes(BaseModel):
    content_like_id : int
    dir : int      
    

class LikesResponse(BaseModel):
    id: int
    email: EmailStr
    content_like_id : int

class Likes2(BaseModel):
    id: int
    email: EmailStr

class DisLikes(BaseModel):
    content_dislike_id : int
    dir : int      
    

class DisLikesResponse(BaseModel):
    id: int
    email: EmailStr
    content_dislike_id : int

class DisLikes2(BaseModel):
    id: int
    email: EmailStr
    