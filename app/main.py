from fastapi import FastAPI, HTTPException
from app.models import User
from app.database import get_user_by_id

app = FastAPI()

@app.get("/user/{user_id}")
async def read_user(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "name": user.name}

@app.get("/test")
async def getTest():
    return "hello world"


def aaa(aaa):
    print("aaaa")