from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

#each instance of NewsItem is a new row
class NewsItem(Base):
    _tablename_ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    link = Column(String, unique=true)
    source = Column(String)
    published = Column(DateTime)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
