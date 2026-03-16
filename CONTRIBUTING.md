# Contributing to Analytix Engine

Thanks for your interest in contributing! 🎉

## Development Setup

```bash
git clone https://github.com/your-org/analytix-engine.git
cd analytix-engine
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
```

## Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests: `pytest -v`
5. Run linting: `ruff check . && black --check .`
6. Commit with a clear message
7. Push and open a Pull Request

## Code Style

- We use **Black** for formatting and **Ruff** for linting
- Type hints are required for all public functions
- Tests are required for new features

## Commit Messages

Follow conventional commits:
- `feat: add new endpoint`
- `fix: handle empty arrays`
- `docs: update API examples`
- `test: add edge case coverage`
