from apscheduler.schedulers.background import BackgroundScheduler
from db import SessionLocal
from rss_fetcher import fetch_and_store_news

def start_scheduler():

    scheduler = BackgroundScheduler()

    def job():
        db = SessionLocal()
        fetch_and_store_news(db)
        db.close()

    scheduler.add_job(job, 'interval', minutes=5)
    scheduler.start()