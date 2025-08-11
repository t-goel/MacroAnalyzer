import feedparser
from sqlalchemy.orm import Session
from models import NewsItem
from datetime import datetime
from dateutil import parser as date_parser

RSS_Feeds = {
    "Federal Reserve" : "https://www.federalreserve.gov/feeds/press_all.xml",
    "Financial Times" : "https://www.ft.com/world?format=rss",
    "Wall Street Journal" : "https://feeds.content.dowjones.io/public/rss/RSSMarketsMain"
}

def fetch_and_store_news (db: Session):
    for source, url in RSS_Feeds.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            exists = db.query(NewsItem).filter_by(link=entry.link).first()
            if not exists:
                news = NewsItem (
                    title=entry.title,
                    link = entry.link,
                    source = entry.source,
                    summary=entry.get("summary", ""),
                    published=date_parser.parse(entry.published)
                )
                db.add(news)
    db.commit()