from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Load .env file
load_dotenv()

# Read Environment Variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Debugging
print("DB_USER =", DB_USER)
print("DB_HOST =", DB_HOST)
print("DB_PORT =", DB_PORT)
print("DB_NAME =", DB_NAME)

# Database URL
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("DATABASE_URL =", DATABASE_URL)

# SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=True
)

# Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Test Database Connection
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("\n✅ Database Connected Successfully!")
except Exception as e:
    print("\n❌ Database Connection Failed!")
    print("Error:", e)