from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import auth
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from contextlib import asynccontextmanager

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
    )

app.include_router(auth.router,  prefix="/api/v1")

@app.get("/health", tags=["Health"])
async def health_check():
    return {"message": "Service is running"}

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Ivaana Designers"}