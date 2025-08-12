from fastapi import FastAPI
from scheduler import start_scheduler
from models import Base
from db import engine

app = FastAPI()


start_scheduler()

@app.get("/")
def root():
    return {"message": "MacroFactor API is live and fetching news"}