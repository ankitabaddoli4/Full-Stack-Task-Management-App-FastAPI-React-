from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1 import auth, users, tasks
from src.core.database import Base, engine

app = FastAPI()

# ✅ CORS (FRONTEND CONNECTION FIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later change to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)

# ✅ ROUTES
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

# ✅ HOME ROUTE
@app.get("/")
def home():
    return {"message": "API is running 🚀"}