from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, constr


class UserRegister(BaseModel):
    user_id: constr(min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_\-]+$") # type: ignore
    password: constr(min_length=8) # type: ignore


class UserLogin(BaseModel):
    user_id: str
    password: str


class ProfileUpdate(BaseModel):
    display_name: Optional[constr(min_length=1, max_length=64)] = None # type: ignore
    icon_url: Optional[str] = None
    bio: Optional[constr(max_length=280)] = None # type: ignore


class UserProfile(BaseModel):
    user_id: str
    display_name: str
    icon_url: Optional[str] = None
    bio: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")
