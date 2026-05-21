from os import getenv

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

MONGO_URI = getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["title"]


def ensure_indexes() -> None:
    try:
        db.users.create_index("user_id", unique=True)
    except ServerSelectionTimeoutError:
        # MongoDB が起動していない場合でもアプリのインポートを妨げない
        pass