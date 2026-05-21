from fastapi import FastAPI
from .database.db import db, ensure_indexes
from .users import router as users_router

app = FastAPI()
app.include_router(users_router, prefix="/users", tags=["users"])

@app.on_event("startup")
async def startup_event() -> None:
    ensure_indexes()


@app.get("/")
def root():
    return {"message": "Hello World"}
@app.get("/posts")
def get_posts():
    posts = list(db.posts.find({}, {"_id": 0}))
    return posts