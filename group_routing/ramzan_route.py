from fastapi import APIRouter
from fastapi import Depends, HTTPException, status  
from pydantic import BaseModel
from group_routing.db_connection import get_database

router = APIRouter(prefix="/ramzan", tags=["Ramzan CRUD"])

class User(BaseModel):
    name: str
    age: int
    cgpa: float

db = get_database()   

@router.post("/create")
def create_item(data: User):
        try:
            collection = db["crud"]
            collection.insert_one(data.model_dump())
            return {
                "message": "Item created successfully",
                "status": "success"
            } 
        except Exception as e:
            return {
                "message": "Invalid ID format",
                "status": "error"
            }  