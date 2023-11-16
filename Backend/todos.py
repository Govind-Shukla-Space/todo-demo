from fastapi import Body,APIRouter
router = APIRouter()
todos = []

# create todo
@router.post('/api/v1/todos')
def createTodo(todo: dict = Body(...)):
    todos.append(todo)
    return todo

# get all todos
@router.get('/api/v1/todos')
def getAllTodos():
    return todos

# get a todo by title
@router.get('/api/v1/todos/{title}')
def getTodoByTitle(title: str):
    response = {"status": 404, "message":"todo not found","data":{}}
    print("title",title)
    for todo in todos:
        print(todo)
        if todo['title'] == title:
            response = {"status": 200, "message":"todo found","data":todo}
            break
    return response

# update a todo by title

# delete a todo by title
@router.delete('/api/v1/todos/{title}')
def getTodoByTitle(title: str):
    response = {"status": 404, "message":"todo not found to delete","data":{}}
    for todo_idx,todo in enumerate(todos):
        if todo['title'] == title:
            todos.pop(todo_idx)
            response = {"status": 200, "message":"todo deleted","data":todo}
            break
    return response