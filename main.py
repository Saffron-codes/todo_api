from typing import Optional
from fastapi import FastAPI,HTTPException,responses
import fastapi
import uvicorn
from db_funcs import DBCrud

from todo import NewTodo, Todo

app = FastAPI()

mytodos = []

@app.get("/")
async def root():
     return responses.RedirectResponse(url='/docs')


@app.post("/api/v1/todos")
async def createTodo(todo:Todo):
    response = DBCrud().createtodo(todo)
    return response

@app.post("/api/v1/todos/update")
async def updateTodo(todo:NewTodo):
    response = DBCrud().updatetodo(todo.userid,todo.todoid,todo.newtodo)
    return response

@app.delete("/api/v1/todos/delete/{userId}")
async def deleteTodo(userId:str,todoId:str):
    return DBCrud().deletetodo(userId,todoId)
@app.get("/api/v1/todos/{userId}")
async def getAllTodo(userId:str,todoId:Optional[str] = None):
    print(userId,todoId)
    if userId !="" and todoId == None:
        print("if block")
        response = DBCrud().getalltodos(userId)
        if response == []:
            raise HTTPException(status_code=404,detail=f"todos of user with id {userId} doesn't exists")
        return response
    else:
        print("else block")
        response = DBCrud().gettodo(userId,todoId)
        if response == {}:
            raise HTTPException(status_code=404,detail=f"todo of user {userId} with id {todoId} doesn't exists")
        return response