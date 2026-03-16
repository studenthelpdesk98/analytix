"""Statistical computation utilities."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def compute_statistics(data: NDArray[np.float64]) -> dict:
    """Compute descriptive statistics for a numeric array."""
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data, ddof=1)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "q25": float(np.percentile(data, 25)),
        "q75": float(np.percentile(data, 75)),
        "skewness": float(_skewness(data)),
        "count": len(data),
    }


def detect_outliers(
    data: NDArray[np.float64],
    method: str = "zscore",
    threshold: float = 2.0,
) -> list[float]:
    """Detect outliers using the specified method."""
    if method == "zscore":
        z_scores = np.abs((data - np.mean(data)) / np.std(data, ddof=1))
        return data[z_scores > threshold].tolist()
    elif method == "iqr":
        q1, q3 = np.percentile(data, [25, 75])
        iqr = q3 - q1
        lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
        return data[(data < lower) | (data > upper)].tolist()
    else:
        raise ValueError(f"Unsupported method: {method}")


def _skewness(data: NDArray[np.float64]) -> float:
    """Calculate Fisher-Pearson skewness coefficient."""
    n = len(data)
    if n < 3:
        return 0.0
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    if std == 0:
        return 0.0
    return float((n / ((n - 1) * (n - 2))) * np.sum(((data - mean) / std) ** 3))
