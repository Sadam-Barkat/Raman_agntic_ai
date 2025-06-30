# Assignment 1: Build a Simple Student API

## Objective
Practice FastAPI basics: routing, query parameters, and request bodies.

## Tasks
1. **Create a FastAPI app** with the following endpoints:
    - `GET /students`: Returns a list of students (use a hardcoded list or dictionary).
    - `GET /student`: Accepts a query parameter `id` (integer). Returns the details of the student with that ID.
    - `POST /student`: Accepts a JSON body with student details (`name`, `age`, `cgpa`). Returns a success message and the student data.
2. **Use Pydantic models** for the student data in the POST endpoint.
3. **Handle validation errors** and return a custom error message if the input is invalid.

## Example student data
```python
students = {
    1: {"name": "Ali", "age": 20, "cgpa": 3.5},
    2: {"name": "Sara", "age": 21, "cgpa": 3.7},
    3: {"name": "John", "age": 22, "cgpa": 3.6}
}
```

## Requirements
- Do not use any database; keep all data in memory (hardcoded).
- Do not add authentication or advanced features.
- Only use what you have learned in class.

---

**Instructions:**
- Implement the endpoints as described above.
- Use the examples and code taught in class as a reference.
- Save your solution in a Python file (e.g., `assignment_1.py`). 