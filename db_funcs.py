import sqlite3
from uuid import uuid1, uuid4
from generator import genNoteId

from todo import Todo

conn = sqlite3.connect("todos.db")

conn.execute('''
    CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY AUTOINCREMENT,userid TEXT,todo TEXT,todoid TEXT)
''')
cur = conn.cursor()
conn.commit()



class DBCrud():
    def __init__(self):
        pass
    def createtodo(self,todo:Todo):
        try:
            id = genNoteId()
            conn.execute("INSERT INTO todos(userid,todo,todoid) \
                values(?,?,?);",(str(todo.userid),todo.todo,id))
            conn.commit()
            return {"id":id}
        except Exception as e:
            print(e)
            return {"message":"error creating todo"}
    
    def getalltodos(self,userId:str):
        todos = []
        try:
            # cur.execute("SELECT * FROM Users WHERE NAME=?",[username])
            res = cur.execute("SELECT * FROM todos WHERE userid=?",[userId])
            # res = conn.execute("SELECT todo FROM todos WHERE userid=(?);",[userId])
            for todo in res:
                print(todo)
                # todos.append(str(todo).split("'")[1])
                # print(todo[0])
                todos.append(
                    {"id":todo[3],
                    "todo":todo[2]
                    })
            # if todos == []:
            #     return {"message":"error retreiving todos"}
            return todos
        except Exception as e:
            print(e)
            return {"message":"error retreiving todo"}
    
    def gettodo(self,userId:str,todoId:str):
        try:
            mytodo = {}
            res = cur.execute("SELECT todo FROM todos WHERE userid=? AND todoid=?",(userId,todoId))
            for todo in res:
                mytodo["todo"] = todo[0]
            return mytodo
        except Exception as e:
            print(e)
            return {"message":"error retreiving todo"}
    def updatetodo(self,userId:str,todoId:str,newtodo):
        try:
            res = cur.execute("UPDATE todos set todo=? where userid=? AND todoid=?",(newtodo,userId,todoId))
            conn.commit()
            if res != None:
                return {"newtodo":newtodo}
            else:
                return {"message":"error updating todo"}  
        except Exception as e:
            print(e)
            return {"message":"error updating todo"}
    
    def deletetodo(self,userId:str,todoId:str):
        try:
            res = cur.execute("DELETE from todos WHERE userid=? AND todoid=?",(userId,todoId))
            conn.commit()
            if res != None:
                return {"message":"deleted"}
            else:
                return {"message":"error deleting todo"}
        except Exception as e:
            print(e)
            return {"message":"error deleting todo"}


# print(DBCrud().gettodo("123saff","XBDjkst;o."))





# print(todo)