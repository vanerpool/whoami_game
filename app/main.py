import random

from fastapi import FastAPI

from pydantic import BaseModel
from starlette import status
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


class GameCreate(BaseModel):
    code: int


class GamePlayer(BaseModel):
    code: int
    nickname: str


class GameCharacter(BaseModel):
    code: int
    nickname: str
    character: str


@app.get("/", response_class=HTMLResponse)
async def read_item():
    with open("static/index.html") as f:
        return f.read()


@app.post(path="/game/create",
          response_model=GameCreate,
          status_code=status.HTTP_201_CREATED)
async def create():
    return {"code": random.randint(0, 10)}


@app.get(path="/game/check",
         response_model=GameCreate,
         status_code=status.HTTP_200_OK)
async def check(game: GameCreate):
    return game
