from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import NewsItem

def delete_old_news(db: Session):
    cutoff_date = datetime.utcnow() - timedelta(days=7)
    old_items = db.query(NewsItem).filter(NewsItem.published < cutoff_date).all()
    
    for item in old_items:
        db.delete(item)
    db.commit()