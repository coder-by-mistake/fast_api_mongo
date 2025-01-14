from fastapi import FastAPI
import uvicorn
from api.router import (
    mng,
    proj
)
from model.db_connection import db_connection
db_connection()
app = FastAPI()

app.include_router(mng)
app.include_router(proj)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)