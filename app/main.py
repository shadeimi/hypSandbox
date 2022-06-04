# server.py

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/prod/{s}")
def homepage(s: int):
    return {"message": s * s}


if __name__ == "__main__":
    uvicorn.run(app)
