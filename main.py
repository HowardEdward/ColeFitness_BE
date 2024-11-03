from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from fastapi import FastAPI
from db.connectDB import Base, connectDB
from controllers import EmployeeController, AccountController

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: set up database connection
    print("Starting up the application...")
    try:
        connect = connectDB()
        if connect:
            print("Database connection established successfully")
            yield
        
    except Exception as e:
        print(f"Error during startup: {e}")
        raise

app = FastAPI(lifespan=lifespan,
              title="Cole Fitness Center")

app.include_router(EmployeeController.router)
app.include_router(AccountController.router)
@app.get("/")
def main():
    return {"message": "Hello World !"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)