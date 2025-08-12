from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

#each instance of NewsItem is a new row
class NewsItem(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link = Column(String, unique=True)
    source = Column(String)
    published = Column(DateTime)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    #nlp fields
    sentiment = Column(Text)
    positive = Column(Float)
    negative = Column(Float)
    neutral = Column(Float)

