from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()





@app.get("/")
def root():
    return({"message":"welcome to root"})

