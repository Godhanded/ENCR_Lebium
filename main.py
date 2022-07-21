from fastapi import FastAPI
from cryptography.fernet import Fernet
#import os
from decouple import config


app = FastAPI()

KEY= bytes(config('KEY'),'utf-8')
fernet= Fernet(KEY)

class Cids(str):
    cids:list


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/{hash}")
def encrypt(hash:Cids):
    hash= hash.split(",")
    hash=map(striper, hash)
   
    cid=map(ccc, hash)
    return list(cid)

@app.post("/d/{hash}")
def decrypt(hash:Cids):
    hash=hash.split(",")
    cid=map(ddd, hash)
    return list(cid)


def ccc(item):
    return fernet.encrypt(item.encode())

def ddd(item):
    foo=bytes(item,'utf-8')
    return fernet.decrypt(foo).decode()

def striper(hash):
    hash=hash.strip('"')
    hash=hash.strip("'")
    return hash