from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(map(str, error["loc"])),  # Converts tuple path to a string
            "message": error["msg"]
        })
    
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": "Validation failed",
            "errors": errors
        }
    )

class Data(BaseModel):
    name:str
    age:int
    cgpa:float

@app.post("/{id}")
def fun(id:int, data:Data):
    try:
        json = {"name":data.name, "age":data.age, "cgpa":data.cgpa}
        return {
            "data":json,
            "message":"successfully inserted into DB",
            "status":200
        }
    except Exception as e:
        return{
            "data":None,
            "message":str(e),
            "status":"error"
        }  
    
