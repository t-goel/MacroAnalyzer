from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,        # Test connections before use
    pool_recycle=3600,         # Recycle connections every hour
    pool_timeout=20,           # Wait 20 seconds for connection
    pool_size=5,               # Number of connections to maintain
    max_overflow=10,           # Additional connections when needed
    echo=False,                # Set to True for SQL debugging
    connect_args={
        "connect_timeout": 10,  # Connection timeout in seconds
        "sslmode": "require"  # Set timezone
    }
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False     # Keep objects accessible after commit
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    """Test database connection"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return True
    except Exception as e:
        print(f"Database connection test failed: {e}")
        return False