from fastapi import FastAPI
from group_routing.ramzan_route import router as ramzan_route
from group_routing.fruits_route import router as fruits_route

app = FastAPI()
# Include the router
app.include_router(ramzan_route)
app.include_router(fruits_route)