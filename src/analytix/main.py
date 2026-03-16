"""Analytix Engine — Application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from analytix.api.routes import router as api_router

app = FastAPI(
    title="Analytix Engine",
    description="High-performance data analytics API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"service": "analytix-engine", "version": "0.1.0", "status": "healthy"}
