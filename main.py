from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from db.connectDB import Base, connectDB
import os
from pathlib import Path
from dotenv import load_dotenv
from controllers import UserController

# Load environment variables
dotenv_path = Path("environment/.env")
load_dotenv(dotenv_path=dotenv_path)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: set up database connection
    print("Starting up the application...")
    try:
        connect = connectDB()
        app.include_router(UserController.router)
        if connect:
            print("Database connection established successfully")
            yield
        
    except Exception as e:
        print(f"Error during startup: {e}")
        raise

app = FastAPI(lifespan=lifespan,
              title="Cole Fitness Center")

@app.get("/")
def main():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)