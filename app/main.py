from fastapi import FastAPI
from .router import user_router
from app.router import user

app = FastAPI()

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}