from dbconn import *

ROUTE = '/list/'


class TodoList:
    def createList(request):
        name = request.form.get("name")
        return create('lists', {"name": name, "items": {}})
    
    def getList(request):
        name = request.form.get("name")
        vals = read('lists')
        for id in vals:
            if vals[id]["name"] == name:
                return vals[id]
        raise Exception(f"{name} does not exist")
    
    def deleteList(request):
        name = request.form.get("name")
        vals = read('lists')
        for id in vals:
            if vals[id]["name"] == name:
                delete('lists', id)
                return
        raise Exception(f"{name} does not exist")
    
    def addItem(request):
        name = request.form.get("name")
        item = request.form.get("item")
        vals = read('lists')
        for id in vals:
            if vals[id]["name"] == name:
                l = vals[id]
                length = len(l['items'])
                l['items'][length + 1] = item
                return update('lists', id, l)
        raise Exception(f"{name} does not exist")
    
    def removeItem(request):
        name = request.form.get("name")
        item_number = request.form.get("item")
        vals = read('lists')
        for id in vals:
            if vals[id]["name"] == name:
                l = vals[id]
                try:
                    l['items'].pop(item_number)
                except:
                    break
                return update('lists', id, l)
        raise Exception(f"{name} does not exist")