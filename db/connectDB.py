import logging
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv
dotenv_path = Path("environment/.env")
load_dotenv(dotenv_path=dotenv_path)

#Setup Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

# Log to Console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler("logs\\cpy-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

Base = declarative_base()
engine = create_engine(os.environ.get("DB_URL"))


def connectDB(attempts=5, delay=3):
    attempt = 1
    while attempt <= attempts:
        try:
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            if engine:
                Base.metadata.create_all(engine)
                db = SessionLocal()
                logger.info("Connected to database")
                return db

        except (Exception) as error:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger.info("Failed to connect, exiting without a connection: %s", error)
                return None
            logger.info(
                "Connection failed: %s. Retrying (%d/%d)...",
                error,
                attempt,
                attempts-1,
            )
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
        finally:
            db.close()

if __name__ == "__main__":
    connectDB() 