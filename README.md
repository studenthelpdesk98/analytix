<div align="center">

# 🚀 Analytix Engine

**A high-performance data analytics API built for modern data teams.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Getting Started](#getting-started) • [Features](#features) • [API Docs](#api-documentation) • [Contributing](#contributing)

</div>

---

## Overview

Analytix Engine is a lightweight, extensible analytics API that transforms raw data into actionable insights. Built with FastAPI and pandas, it provides RESTful endpoints for statistical analysis, anomaly detection, and predictive modeling.

## Features

- 📊 **Statistical Analysis** — Descriptive stats, distributions, and correlations via API
- 🔍 **Anomaly Detection** — Isolation Forest & Z-score based outlier detection
- 📈 **Trend Forecasting** — Time-series decomposition and basic forecasting
- ⚡ **High Performance** — Async processing with Redis caching
- 🔐 **Auth Ready** — JWT-based authentication out of the box
- 📄 **Auto Docs** — OpenAPI/Swagger documentation at `/docs`

## Getting Started

### Prerequisites

- Python 3.10+
- Redis (optional, for caching)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/analytix-engine.git
cd analytix-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn src.analytix.main:app --reload
```

### Quick Example

```python
import requests

# Analyze a dataset
response = requests.post("http://localhost:8000/api/v1/analyze", json={
    "data": [12, 15, 18, 22, 14, 30, 16, 19],
    "operations": ["describe", "detect_outliers"]
})

print(response.json())
# {"mean": 18.25, "std": 5.70, "outliers": [30], ...}
```

## API Documentation

Once running, interactive docs are available at:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/analyze` | POST | Run statistical analysis |
| `/api/v1/detect` | POST | Detect anomalies |
| `/api/v1/forecast` | POST | Generate time-series forecast |
| `/api/v1/health` | GET | Service health check |

## Architecture

```
src/analytix/
├── api/          # Route handlers
├── models/       # Pydantic schemas & ML models
├── utils/        # Helpers, config, logging
└── main.py       # Application entrypoint
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with ❤️ by the Analytics Team</sub>
</div>
