from fastapi import APIRouter
from fastapi import Depends, HTTPException, status  
from pydantic import BaseModel
from group_routing.db_connection import get_database

router = APIRouter(prefix="/fruits", tags=["Fruits CRUD"])

class Fruit(BaseModel):
    name: str
    color: str
    weight: float

db = get_database()    

@router.post("/create")
def create_fruit(data: Fruit):  
    try:
        collection = db["fruits"]
        collection.insert_one(data.model_dump())
        return {
            "message": "Fruit created successfully",
            "status": "success"
        } 
    except Exception as e:
        return {
            "message": "Error creating fruit",
            "status": "error",
            "error": str(e)
        }
