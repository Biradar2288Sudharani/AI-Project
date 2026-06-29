from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload_routes import router as upload_router
#from app.routes.discharge_routes import router as discharge_router
from app.routes.summary_routes import router as summary_router

app = FastAPI(
    title="DScribe AI Discharge Summary Agent",
    description="Agentic AI System for Clinical Discharge Summaries",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(summary_router)

@app.get("/")
async def home():
    return {
        "message": "DScribe AI Agent Running Successfully",
        "status": "success"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI Backend",
        "version": "1.0.0"
    }