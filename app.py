from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import ai
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    message: str


@app.get("/api/test")
async def test():
    return "Hello World"


@app.post("/api/chat")
async def chat(data: Item):
    return ai(data.message)
