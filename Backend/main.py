from fastapi import FastAPI, Body
import todos
import auth
app = FastAPI()
app.include_router(todos.router)
app.include_router(auth.router)


@app.get('/')
def greet():
    return "3rd year elite intro to fastapi"


@app.get('/')
def greet2():
    return "overriden"


@app.get('/hello/{username}')
def say_hello(username: str):
    return "hello " + username


@app.get('/hello2/{username}')
def say_hello2(username: str):
    return {"username": username}
