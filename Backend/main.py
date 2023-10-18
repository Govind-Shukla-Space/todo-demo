from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def greet():
    return "3rd year eleite intro to fastapi1"
@app.get('/hello/{username}')
def say_hello(username:str):
    return "hello"+username