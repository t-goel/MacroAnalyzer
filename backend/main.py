from fastapi import FastAPI, Depends
from sqlalchemy import func
from scheduler import start_scheduler
from db import get_db
from sqlalchemy.orm import Session
from models import NewsItem

app = FastAPI(title="Macrofactor News App")


start_scheduler()

@app.get("/")
def root():
    return {"message": "MacroFactor API is live and fetching news"}


@app.get("/news/sentiment")
def get_sentiment_data(db: Session = Depends(get_db)):
    sentiment_counts = (
        db.query(NewsItem.sentiment, func.count(NewsItem.id))
        .group_by(NewsItem.sentiment)
        .all()
    )

    result = {}
    for sentiment, count in sentiment_counts:
        result[sentiment] = count

    return result
