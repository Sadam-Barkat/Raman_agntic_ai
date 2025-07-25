from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv
import os



from bson import ObjectId

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URL")

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client["Ramzan_database"] 
collection = db["crud"]

class User(BaseModel):
    name: str
    age: int
    cgpa: float


# FastAPI app
app = FastAPI()

# GET all items
@app.get("/")
def get_all_items():
    try:
        documents = collection.find()
        items = []
        for doc in documents:
            item = {
                "id": str(doc["_id"]),
                "name": doc.get("name"),
                "age": doc.get("age"),
                "cgpa": doc.get("cgpa"),
            }
            items.append(item)

        return{
            "data": items,
            "message": "All items retrieved successfully",
            "status": "success"
        }    
    except Exception as e:
        return {
            "message": "Error retrieving items",
            "status": "error",
            "error": str(e)
        }

@app.post("/")
def create_item(data: User):
    try:
        collection.insert_one(data.model_dump())
        return {
            "message": "Item created successfully",
            "status": "success"
        }
    except Exception as e:
        return {
            "message": "Error creating item",
            "status": "error",
            "error": str(e)
        }
    
@app.get("/{id}")
def get_item(id: str):
    try:
        try:
            obj_id = ObjectId(id)
        except Exception:
            return {
                "message": "Invalid id format",
                "status": "error"
            }
        document = collection.find_one({"_id": obj_id})
        if document:
            item = {
                "id": str(document["_id"]),
                "name": document.get("name"),
                "age": document.get("age"),
                "cgpa": document.get("cgpa"),
            }
            return {
                "data": item,
                "message": "Item retrieved successfully",
                "status": "success"
            }
        else:
            return {
                "message": "Item not found",
                "status": "error"
            }
    except Exception as e:
        return {
            "message": "Error retrieving item",
            "status": "error",
            "error": str(e)
        }    
