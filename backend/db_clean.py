from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import NewsItem

search_days = 1

def delete_old_news(db: Session):
    cutoff_date = datetime.utcnow() - timedelta(days=search_days)
    old_items = db.query(NewsItem).filter(NewsItem.published < cutoff_date).all()
    count = 0
    for item in old_items:
        count += 1
        db.delete(item)
    db.commit()
    print(f"\n✅ Deleted {count} old entries!")