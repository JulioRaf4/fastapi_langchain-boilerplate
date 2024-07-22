import os 
import uvicorn
from fastapi import FastAPI
from service.routers import exemplo 

app = FastAPI()

app.include_router(exemplo.router)

if __name__ == "__main__":
    uvicorn.run("service.main:app", host="127.0.0.1", port=8000, reload=True)
