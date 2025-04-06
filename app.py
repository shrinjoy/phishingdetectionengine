from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from levelone_check import check
from levelone_check import emailpayload
app = FastAPI()
@app.get("/")
def root():
    return({"message":"welcome to root"})

@app.post("/check/")
def startemailcheck(payload:emailpayload):
    return check(payload)