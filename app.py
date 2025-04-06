from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from levelone_check import *
app = FastAPI()
@app.get("/")
def root():
    return({"message":"welcome to root"})

@app.post("/check/")
def startemailcheck(payload:emailpayload):
    return levelone_check(payload)