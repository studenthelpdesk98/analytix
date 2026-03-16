"""API route handlers for analytics operations."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
import numpy as np
from analytix.models.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    AnomalyRequest,
    AnomalyResponse,
    HealthResponse,
)
from analytix.utils.stats import compute_statistics, detect_outliers

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Service health check endpoint."""
    return HealthResponse(status="healthy", version="0.1.0")


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest):
    """Run statistical analysis on provided data."""
    if not request.data:
        raise HTTPException(status_code=400, detail="Data array cannot be empty")

    results = compute_statistics(np.array(request.data))
    return AnalysisResponse(results=results, sample_size=len(request.data))


@router.post("/detect", response_model=AnomalyResponse)
async def detect_anomalies(request: AnomalyRequest):
    """Detect anomalies in provided data using specified method."""
    if not request.data:
        raise HTTPException(status_code=400, detail="Data array cannot be empty")

    outliers = detect_outliers(
        np.array(request.data), method=request.method, threshold=request.threshold
    )
    return AnomalyResponse(
        outliers=outliers,
        count=len(outliers),
        method=request.method,
    )
