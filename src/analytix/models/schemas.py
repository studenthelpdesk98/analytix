"""Pydantic models for request/response validation."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    data: list[float] = Field(..., min_length=1, description="Numeric data array")
    operations: list[str] = Field(
        default=["describe"], description="Analysis operations to perform"
    )


class AnalysisResponse(BaseModel):
    results: dict
    sample_size: int


class AnomalyRequest(BaseModel):
    data: list[float] = Field(..., min_length=1)
    method: str = Field(default="zscore", pattern="^(zscore|iqr|isolation_forest)$")
    threshold: float = Field(default=2.0, gt=0)


class AnomalyResponse(BaseModel):
    outliers: list[float]
    count: int
    method: str


class HealthResponse(BaseModel):
    status: str
    version: str
