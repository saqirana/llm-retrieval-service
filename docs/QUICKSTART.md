# Quick Start Guide

This guide will help you get the LLM Retrieval Service up and running in minutes.

## Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- Git
- API keys for OpenAI and/or Anthropic (optional for development)

## Installation

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/saqirana/llm-retrieval-service.git
cd llm-retrieval-service

# Run the setup script
./setup.sh
```

The setup script will:
- Create a virtual environment
- Install all dependencies
- Set up pre-commit hooks
- Create .env file from template
- Optionally start Docker services

### Option 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/saqirana/llm-retrieval-service.git
cd llm-retrieval-service

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Copy environment file
cp .env.example .env

# Edit .env with your configuration
nano .env  # or use your preferred editor

# Install pre-commit hooks
pre-commit install
```

## Configuration

Edit the `.env` file and add your API keys:

```bash
# Required for LLM features
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Required for vector search
PINECONE_API_KEY=your-key-here
PINECONE_ENVIRONMENT=us-east-1-aws

# Update secret key for production
SECRET_KEY=$(openssl rand -hex 32)
```

## Running the Application

### Using Docker (Recommended for Development)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down
```

### Without Docker

```bash
# Start PostgreSQL and Redis (if you have them installed locally)
# Or update .env to point to remote instances

# Activate virtual environment
source .venv/bin/activate

# Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Accessing the Application

Once running, you can access:

- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Documentation (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **API Base URL**: http://localhost:8000/api/v1

## Testing the API

### Using the Interactive Documentation

1. Navigate to http://localhost:8000/docs
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Fill in the parameters
5. Click "Execute"

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Register a user
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePassword123!",
    "full_name": "Test User"
  }'

# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=SecurePassword123!"

# Use the token from login response
export TOKEN="your-access-token-here"

# Upload a document
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@/path/to/document.pdf"

# Chat with streaming
curl -N -X POST "http://localhost:8000/api/v1/chat/stream" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is artificial intelligence?",
    "use_rag": true
  }'
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_auth.py

# Run with markers
pytest -m unit
pytest -m "not slow"
```

### Code Quality

```bash
# Format code
black .

# Lint code
ruff check .

# Type checking
mypy app/

# Run all pre-commit hooks
pre-commit run --all-files
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Common Issues

### Port Already in Use

If port 8000 is already in use:
```bash
# Option 1: Use a different port
uvicorn main:app --reload --port 8001

# Option 2: Kill the process using the port
lsof -ti:8000 | xargs kill -9
```

### Database Connection Error

Ensure PostgreSQL is running:
```bash
# Check Docker services
docker-compose ps

# Restart PostgreSQL
docker-compose restart postgres
```

### Module Not Found Error

Ensure you're in the virtual environment:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Next Steps

- Read the [Architecture Documentation](docs/ARCHITECTURE.md)
- Check out the [API Documentation](docs/API.md)
- Review [Contributing Guidelines](docs/CONTRIBUTING.md)
- Explore the [Deployment Guide](docs/DEPLOYMENT.md)

## Getting Help

- GitHub Issues: https://github.com/saqirana/llm-retrieval-service/issues
- Email: saqi_rana@hotmail.com

Happy coding! 🚀

