from fastapi import FastAPI
from models import TodoModel  ,TodoHelper
from dotenv import load_dotenv
import os 
load_dotenv()
from config import mongo_db
from bson import ObjectId

app = FastAPI()

# create collection
TodoCollection = mongo_db['Todo']

@app.get("/")
def home():
    return {
        "msg" : "Server is running perfectly..."
    }

@app.get("/")
async def index_view():
    data = await TodoCollection.find().to_list(length=None)
    
    all_todos = []
    for todo in data:
        all_todos.append(TodoHelper(todo))

    return all_todos


@app.post("/create")
async def create_data(new_data : TodoModel):
    result = await TodoCollection.insert_one(dict(new_data))
    print(result)
    return {
        "msg" : new_data
    }



@app.delete("/delete/{id}")
async def deletebyID(id : str):
    data =  await TodoCollection.find_one_and_delete({"_id" : ObjectId(id)})
    print(data)
    return {
        "msg" : "Todo deletd successfuly..."
    }



@app.put("/upadate/{id}")
async def upadatebyID(id : str , data : TodoModel):
    data =  await TodoCollection.find_one_and_update({"_id" : ObjectId(id)} , {
        "$set" : dict(data)
    })
    print(data)
    return {
        "msg" : "Todo updated successfuly..."
    }




