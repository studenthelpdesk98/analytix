"""Tests for statistical utility functions."""

import numpy as np
import pytest
from analytix.utils.stats import compute_statistics, detect_outliers


class TestComputeStatistics:
    def test_basic_statistics(self):
        data = np.array([10, 20, 30, 40, 50])
        result = compute_statistics(data)
        assert result["mean"] == 30.0
        assert result["median"] == 30.0
        assert result["min"] == 10.0
        assert result["max"] == 50.0
        assert result["count"] == 5

    def test_single_value(self):
        data = np.array([42.0])
        result = compute_statistics(data)
        assert result["mean"] == 42.0
        assert result["count"] == 1


class TestDetectOutliers:
    def test_zscore_detects_outliers(self):
        data = np.array([10, 12, 11, 13, 12, 100])
        outliers = detect_outliers(data, method="zscore", threshold=2.0)
        assert 100 in outliers

    def test_iqr_detects_outliers(self):
        data = np.array([10, 12, 11, 13, 12, 100])
        outliers = detect_outliers(data, method="iqr", threshold=1.5)
        assert 100 in outliers

    def test_no_outliers(self):
        data = np.array([10, 11, 12, 13, 14])
        outliers = detect_outliers(data, method="zscore", threshold=3.0)
        assert len(outliers) == 0

    def test_invalid_method_raises(self):
        with pytest.raises(ValueError, match="Unsupported method"):
            detect_outliers(np.array([1, 2, 3]), method="invalid")
