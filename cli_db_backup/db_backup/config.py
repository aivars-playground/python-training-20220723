import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import lru_cache  # returns same result when calling with same parameters


load_dotenv()


@lru_cache(maxsize=32)
def engine(db_url=None):
    print(f"request engine for {db_url}")
    db_url = db_url or os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL required")
    print(f"return engine for {db_url}")
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url).connect()


# Returns a session class!!!
@lru_cache(maxsize=32)
def get_session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))


# convenience... use config.session directly
try:
    Session = get_session_class()
except:
    print("ERR: failed creating a session class")
