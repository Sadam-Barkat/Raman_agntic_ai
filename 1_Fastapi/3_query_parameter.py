from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def query(id:Optional[int]=None, name:Optional[str]=None):
    json = {1:{'sadam':"sadam", 'cgpa':3.55, 'age':25},
            2:{'ramzan':"ramzan",'cgpa':3.5, 'age':22},
            3:{'hussain':"hussain",'cgpa':3.6, 'age':23}            
            }
    if id:
        data = json[id][name]
    return {"data":data}