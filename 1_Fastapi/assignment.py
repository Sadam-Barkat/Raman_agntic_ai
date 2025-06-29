from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, conlist
from typing import Optional
import re
from email_validator import validate_email, EmailNotValidError

app = FastAPI()

class Form(BaseModel):
    name: str
    age: int
    email: str
    courses: list[str]

class Email(BaseModel):
    email: str

@app.get('/students/{studentid}')
def get_student(studentid: int, include_grade: bool, semester: Optional[str]= None):
    try:
        if studentid < 1000 or studentid > 9999:
            raise HTTPException(status_code=422, detail="invalid StudentId")
            raise ValueError("Invalid Id")
        if semester is not None and not re.match(r"^(fall|spring|summer)\d{4}$", semester):
            raise HTTPException(status_code=422, detail="invalid semester")

        return {
            "studentId":studentid,
            "status":"success",
            "include_grade":include_grade,
            "semester":semester
        }    

    except Exception as e:
        return {
            "message":str(e),
            "status":"error",
            "data":None
        }

@app.post('/student/register') 
def student_register(form: Form):
    try:
        if(len(form.name) > 50 or form.name.replace(" ", "").isalpha()==False): 
            raise ValueError("Name is invalid") 
        if (form.age < 18 or form.age > 30):
            raise ValueError("Invalid age") 
        email = validate_email(form.email)   
        if(email==False):
            raise ValueError("Invalid email")
        if (len(form.courses) < 1 or len(form.courses) > 5):
            raise ValueError("Invalid number of course")
        seen = set()
        for course in form.courses:
            if not(5<= len(course) <=30):
                raise("course name is invalid")
        return {
            'status':'success',
            'data':form
        }   
    except Exception as e:
        return {
            'status':'error',
            'message':str(e),
            'data':None
        }   

from fastapi import FastAPI, HTTPException
from email_validator import validate_email, EmailNotValidError

@app.put('/students/{studentid}/{email}')
def update_email(studentid: int, email: str):
    try:
        if studentid < 1000 or studentid > 9999:
            raise HTTPException(status_code=422, detail="Invalid student id")
        
        # ✅ Correct email validation
        validate_email(email)

        return {
            'status': 'success',
            'message': 'Email updated successfully',
            'data': {
                'studentid': studentid,
                'email': email
            }
        }

    except EmailNotValidError:
        raise HTTPException(status_code=422, detail="Invalid email")
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
            'data': None
        }
