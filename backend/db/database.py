from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker 


# database file
DATABASE_URL = "sqlite:///./test.db"

# engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# session (talk to database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
