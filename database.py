from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///WClouds.db"

# engine erstellen
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Session Factory erstellen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# basisklasse für die Modelle
Base = declarative_base()

# Für Foreign Keys
@event.listens_for(engine, "connect")
def _fk_on(conn, _):
  conn.execute("PRAGMA foreign_keys=ON")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()