from apscheduler.schedulers.background import BackgroundScheduler
from db import SessionLocal, test_connection
from rss_fetcher import fetch_and_store_news
import time

def start_scheduler():
    scheduler = BackgroundScheduler()

    def job():
        print("🔄 Running RSS fetch job...")
        
        if not test_connection():
            print("❌ Database connection test failed, skipping RSS fetch")
            return
        
        db = SessionLocal()
        # print("cp 1")
        try:
            fetch_and_store_news(db)
            # print("cp 2")
        except Exception as e:
            print(f"RSS fetch failed: {e}")
            try:
                db.rollback()
            except:
                pass
        finally:
            try:
                db.close()
            except:
                pass
            # print("cp 3")

    scheduler.add_job(job, 'interval', minutes=1)
    scheduler.start()
    print("Scheduler started, RSS feeds will be fetched every 10 minutes")