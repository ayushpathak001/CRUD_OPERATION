from pydantic import BaseModel
from typing import Union
from datetime import datetime

class TodoModel(BaseModel):
    title : str
    desc : str
    is_complete : Union[bool , None] = False
    created_at : Union[datetime , None] = datetime.utcnow()



def TodoHelper(data):
    return {
        "id" : str(data["_id"]), 
        "title" : data["title"] , 
        "desc" : data["desc"] , 
        "created_at" : data['created_at']
    }