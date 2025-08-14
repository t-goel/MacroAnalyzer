from fastapi import FastAPI, Depends
from sqlalchemy import func
from scheduler import start_scheduler
from db import get_db
from sqlalchemy.orm import Session
from models import NewsItem
from rss_fetcher import RSS_Feeds

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
    #returns list of tuples

    result = {}
    for sentiment, count in sentiment_counts:
        result[sentiment] = count

    return result

@app.get("/news/sources")
def get_source_data(db: Session = Depends(get_db)):
    result = []
    #list of dictionaries
    for feed in RSS_Feeds:
        query = (
            db.query(NewsItem.sentiment, func.count(NewsItem.id))
            .filter(NewsItem.source == feed)
            .group_by(NewsItem.sentiment)
            .all()
        )

        source = {    
            "negative": 0,
            "positive": 0,
            "neutral": 0
            }
        #default values
        
        for sent, count in query:
            source[sent] = count

        source["source"] = feed
        
        result.append(source)

    return result
