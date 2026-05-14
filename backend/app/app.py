from fastapi import FastAPI
from backend.app.database.db import db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
@app.get("/posts")
def get_posts():
    posts = list(db.posts.find({}, {"_id": 0}))
    return posts