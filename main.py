from fastapi import FastAPI
from app.routers import user
from app.db.database import Base, engine
import uvicorn

##This is a test comment
##This is my second test comment Emma
##This is a test comment 2
##This is a test comment 3
##This is a test comment 4

def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
