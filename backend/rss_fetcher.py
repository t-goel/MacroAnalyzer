import feedparser
from sqlalchemy.orm import Session
from db import SessionLocal
from db_clean import delete_old_news
from sqlalchemy import text
from models import NewsItem
from datetime import datetime, timedelta, timezone
from dateutil import parser as date_parser
import ssl
from db_clean import search_days
from nlp.sentiment import analyze_batch

# Only bypass SSL in development
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


RSS_Feeds = {
    "Federal Reserve" : "https://www.federalreserve.gov/feeds/press_all.xml",
    "Financial Times" : "https://www.ft.com/world?format=rss",
    "Wall Street Journal" : "https://feeds.content.dowjones.io/public/rss/RSSMarketsMain",
    "Federal Reserve Bank of St. Louis" : "https://www.stlouisfed.org/rss/page%20resources/publications/blog-entries",
    "Center for Economic and Policy Research" : "https://cepr.org/rss/news",
    "BNP Paribas Economic Research" : "https://economic-research.bnpparibas.com/RSS/en-US/Eco-Flash",
    "US Bureau of Economic Analysis" : "https://apps.bea.gov/rss/rss.xml",
    "CNBC" : "https://www.cnbc.com/id/10001147/device/rss/rss.html",
    
    
}

def fetch_and_store_news(db: Session):

    # Test database connection first
    try:
        db.execute(text("SELECT 1"))
        print("✅ Database connection successful")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("🔧 Please check your database connection and try again")
        return
    
    total_new_articles = 0
    new_entries = []

    for source_name, url in RSS_Feeds.items():
        print(f"\n🔍 Processing {source_name}")
        
        try:
            # Parse the RSS feed
            feed = feedparser.parse(url)
            
            if not feed.entries:
                print(f"❌ No entries found for {source_name}")
                continue
                
            
            
            # Process each entry

            this_new_articles = 0

            for entry in feed.entries:
                try:
                    # Check if article already exists
                    exists = db.query(NewsItem).filter_by(link=entry.link).first()
                    
                    if not exists:
                        
                        published_date = datetime.now()
                        if hasattr(entry, 'published'):
                            published_date = date_parser.parse(entry.published)


                        if published_date < datetime.now(timezone.utc) - timedelta(days=search_days):
                            continue
                        
                        

                        # Create new news item
                        new_entries.append({
                            "title":entry.title,
                            "link":entry.link,
                            "source":source_name,
                            "summary":entry.get("summary", ""),
                            "published":published_date
                        })

                        this_new_articles += 1
                        
                except Exception as e:
                    print(f"⚠️  Error processing entry from {source_name}: {e}")
                    continue

            total_new_articles += this_new_articles

            print(f"✅ Found {this_new_articles} new entries")
            
        except Exception as e:
            print(f"❌ Error fetching {source_name}: {e}")
            continue
    

    #batch analyse and add to db
    if total_new_articles > 0:
        texts = [f"{e['title']} {e['summary']}" for e in new_entries]
        sentiments = analyze_batch(texts)

        for entry, sent in zip(new_entries, sentiments):
            news = NewsItem(
                title=entry["title"],
                link=entry["link"],
                source=entry["source"],
                summary=entry["summary"],
                published=entry["published"],
                sentiment=sent["sentiment"],
                positive=float(sent["positive"]),
                negative=float(sent["negative"]),
                neutral=float(sent["neutral"])
            )
            db.add(news)
    
    
        try:
            db.commit()
            print(f"\n✅ Successfully committed {total_new_articles} new articles to database")
        except Exception as e:
            print(f"\n❌ Error committing to database: {e}")
            db.rollback()
    else:
        print("\n📰 No new articles to commit")

    print(f"\nProcessed articles from the past {search_days} days!")
    
    delete_old_news(db)