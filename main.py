from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')

#Flask way

@storage.get('/')
def index():
    return "Hello I'm Jacques NZAMUBONA, This is my FAST-API"

@storage.get('/today')#rout with the Get Method
def today():
    return str(datetime.now())


@storage.get('/mynames')#rout with the Get Method
def names(First_Name: bool=False, Last_Name: bool=False):
    Full_Name=""
    if First_Name:
        Full_Name +='Jacques'
    if Last_Name:
        Full_Name += 'NZAMUBONA'
    
    
    return Full_Name