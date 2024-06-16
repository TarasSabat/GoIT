from pydantic import BaseModel, Field


class User(BaseModel):
    username: str
    hashed_password: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str = Field(default="bearer")