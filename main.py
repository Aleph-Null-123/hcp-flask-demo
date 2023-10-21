import os
from todoList import TodoList, ROUTE
from flask import Flask, request, session
from flask_cors import CORS # optional


app = Flask(__name__)
app.secret_key = 'l' # optional

CORS(app) # optional

@app.route("/", methods = ['GET'])
def hello_world():
    return f"hello world"

@app.route(ROUTE + 'createList', methods = ['POST'])
def createList():
    return TodoList.createList(request)

@app.route(ROUTE + 'getList', methods = ['POST'])
def getList():
    return TodoList.getList(request)

@app.route(ROUTE + 'deleteList', methods = ['POST'])
def deleteList():
    return TodoList.deleteList(request)

@app.route(ROUTE + 'addItem', methods = ['POST'])
def addItem():
    return TodoList.addItem(request)

@app.route(ROUTE + 'removeItem', methods = ['POST'])
def removeItem():
    return TodoList.removeItem(request)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
