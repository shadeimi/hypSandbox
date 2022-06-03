# server.py

import uvicorn
from fastapi import FastAPI
from .funct import factorial, palindrome

app = FastAPI()


@app.get("/api/prod/{s}")
def homepage(s: int):
    return {"message": s * s}


@app.get("/api/fact/{s}")
def fact(s: int):
    return {"message": factorial(s)}


@app.get("/api/palindrome/{s}")
def pal(s: int):
    return {"message": palindrome(s)}


if __name__ == "__main__":
    uvicorn.run(app)
