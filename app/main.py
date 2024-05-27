from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

DATA_FILE = Path("data/users.json")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
        return users
    return []

@app.post("/users")
def create_user(user: dict):
    users = []
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    users.append(user)
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)
    return user
