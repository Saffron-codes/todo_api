from typing import Optional

from pydantic import BaseModel

class Todo(BaseModel):
    userid:str
    todo:str


class NewTodo(BaseModel):
    userid:str
    todoid:str
    newtodo:str