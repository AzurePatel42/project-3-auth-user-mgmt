from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.users.routes import router as user_router

app = FastAPI(
    title="Project 3 - Auth & User Management API",
    version="1.0.0",
    description="Authentication + User CRUD microservice"
)

# Include routers
app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Project 3 Auth & User Management API is running"}
