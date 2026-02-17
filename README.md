# 🚀 LLM Retrieval Service - Enterprise RAG System

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

A production-ready, enterprise-grade **Retrieval-Augmented Generation (RAG)** system built with modern AI/ML stack. This service provides intelligent document retrieval, real-time chat streaming, and scalable vector search capabilities.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Documentation](#-api-documentation)
- [Deployment](#-deployment)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Monitoring & Observability](#-monitoring--observability)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### Core Capabilities
- 🤖 **Advanced RAG System**: Context-aware retrieval using state-of-the-art embedding models
- 💬 **Real-time Chat Streaming**: Server-Sent Events (SSE) for responsive user experience
- 🔍 **Vector Search**: High-performance similarity search with FAISS and Pinecone
- 📚 **Multi-format Document Processing**: Support for PDF, DOCX, TXT, Markdown, and more
- 🔄 **Batch Processing**: AWS Glue jobs for large-scale document ingestion
- 🗄️ **Persistent Storage**: PostgreSQL with pgvector for hybrid search

### Enterprise Features
- 🔐 **Authentication & Authorization**: JWT-based security with role-based access control
- 📊 **Analytics & Monitoring**: CloudWatch metrics, custom dashboards, and alerting
- 🚀 **Serverless Deployment**: AWS Lambda with API Gateway integration
- 🐳 **Containerization**: Docker & Docker Compose for local development
- ⚡ **Auto-scaling**: Horizontal pod autoscaling based on load
- 🔧 **Configuration Management**: Environment-based configs with AWS Secrets Manager
- 📝 **Comprehensive Logging**: Structured logging with correlation IDs
- 🧪 **Testing Suite**: Unit, integration, and load tests with 80%+ coverage

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Client Applications                         │
│                     (Web, Mobile, CLI, APIs)                         │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      AWS API Gateway / ALB                           │
│                    (Rate Limiting, Throttling)                       │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      FastAPI Application                             │
│                  (REST API + WebSocket + SSE)                        │
├─────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐             │
│  │   Auth      │  │   Retrieval  │  │   Chat        │             │
│  │   Service   │  │   Service    │  │   Service     │             │
│  └─────────────┘  └──────────────┘  └───────────────┘             │
└────────┬───────────────────┬────────────────┬─────────────────────┘
         │                   │                │
         │                   │                │
    ┌────▼────┐         ┌────▼─────┐    ┌────▼─────┐
    │  Redis  │         │ Pinecone │    │   LLM    │
    │  Cache  │         │  Vector  │    │  OpenAI  │
    └─────────┘         │   DB     │    │  Claude  │
                        └────┬─────┘    └──────────┘
                             │
                        ┌────▼─────┐
                        │PostgreSQL│
                        │ pgvector │
                        └──────────┘
         
┌─────────────────────────────────────────────────────────────────────┐
│                      Data Ingestion Pipeline                         │
├─────────────────────────────────────────────────────────────────────┤
│  S3 Bucket → AWS Glue Job → Document Processing → Vector Store      │
└─────────────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Backend & API
- **FastAPI**: Modern, high-performance web framework
- **Python 3.11+**: Latest Python features and performance improvements
- **Pydantic**: Data validation and settings management
- **SQLAlchemy**: Database ORM with async support
- **Alembic**: Database migration tool

### AI/ML Stack
- **LangChain**: LLM orchestration and chaining
- **OpenAI GPT-4**: Primary language model
- **Anthropic Claude**: Alternative LLM provider
- **Sentence Transformers**: Embedding generation
- **FAISS**: Facebook AI Similarity Search
- **Pinecone**: Managed vector database

### Data & Storage
- **PostgreSQL 15**: Primary relational database
- **pgvector**: PostgreSQL extension for vector similarity search
- **Redis**: Caching and session management
- **AWS S3**: Object storage for documents
- **AWS RDS**: Managed PostgreSQL instance

### AWS Services
- **AWS Lambda**: Serverless compute
- **AWS Glue**: ETL and batch processing
- **AWS API Gateway**: API management and routing
- **AWS CloudWatch**: Monitoring and logging
- **AWS Secrets Manager**: Secure credential storage
- **AWS SQS**: Message queuing
- **AWS EventBridge**: Event-driven architecture

### DevOps & CI/CD
- **Docker & Docker Compose**: Containerization
- **GitHub Actions**: CI/CD pipeline
- **Terraform**: Infrastructure as Code
- **AWS CDK**: Cloud Development Kit
- **Pytest**: Testing framework
- **Black, Ruff**: Code formatting and linting
- **Pre-commit hooks**: Code quality checks

## 📁 Project Structure

```
llm-retrieval-service/
├── .github/
│   └── workflows/
│       ├── ci.yml                      # Continuous Integration
│       ├── cd.yml                      # Continuous Deployment
│       └── quality-checks.yml          # Code quality checks
├── app/
│   ├── __init__.py
│   ├── main.py                         # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py             # Authentication endpoints
│   │   │   │   ├── chat.py             # Chat & streaming endpoints
│   │   │   │   ├── documents.py        # Document management
│   │   │   │   ├── retrieval.py        # RAG retrieval endpoints
│   │   │   │   └── health.py           # Health check endpoints
│   │   │   └── router.py               # API router configuration
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                   # Application configuration
│   │   ├── security.py                 # JWT, OAuth, RBAC
│   │   ├── logging.py                  # Logging configuration
│   │   └── middleware.py               # Custom middleware
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                     # User model
│   │   ├── document.py                 # Document model
│   │   ├── chat.py                     # Chat session model
│   │   └── vector.py                   # Vector embeddings model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py                     # User Pydantic schemas
│   │   ├── document.py                 # Document schemas
│   │   ├── chat.py                     # Chat schemas
│   │   └── retrieval.py                # Retrieval schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm/
│   │   │   ├── __init__.py
│   │   │   ├── openai_service.py       # OpenAI integration
│   │   │   ├── claude_service.py       # Anthropic Claude integration
│   │   │   └── base.py                 # Base LLM interface
│   │   ├── vector/
│   │   │   ├── __init__.py
│   │   │   ├── pinecone_service.py     # Pinecone integration
│   │   │   ├── pgvector_service.py     # PostgreSQL pgvector
│   │   │   └── faiss_service.py        # FAISS local search
│   │   ├── rag/
│   │   │   ├── __init__.py
│   │   │   ├── retriever.py            # RAG retrieval logic
│   │   │   ├── chunker.py              # Document chunking
│   │   │   └── embeddings.py           # Embedding generation
│   │   ├── chat/
│   │   │   ├── __init__.py
│   │   │   ├── chat_service.py         # Chat orchestration
│   │   │   └── streaming.py            # SSE streaming
│   │   └── document/
│   │       ├── __init__.py
│   │       ├── processor.py            # Document processing
│   │       ├── parser.py               # Multi-format parsing
│   │       └── uploader.py             # S3 upload handling
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py                  # Database session management
│   │   ├── base.py                     # Base model class
│   │   └── repositories/
│   │       ├── __init__.py
│   │       ├── user_repo.py
│   │       ├── document_repo.py
│   │       └── chat_repo.py
│   └── utils/
│       ├── __init__.py
│       ├── aws.py                      # AWS SDK utilities
│       ├── cache.py                    # Redis caching
│       └── helpers.py                  # Helper functions
├── aws/
│   ├── lambda/
│   │   ├── requirements.txt
│   │   ├── handler.py                  # Lambda function handler
│   │   └── Dockerfile                  # Lambda container image
│   ├── glue/
│   │   ├── document_ingestion_job.py   # Glue ETL job
│   │   └── requirements.txt
│   └── cloudformation/
│       ├── infrastructure.yml          # CloudFormation templates
│       └── parameters/
│           ├── dev.json
│           ├── staging.json
│           └── prod.json
├── infrastructure/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── modules/
│   │   │   ├── vpc/
│   │   │   ├── rds/
│   │   │   ├── lambda/
│   │   │   ├── s3/
│   │   │   └── api_gateway/
│   │   └── environments/
│   │       ├── dev/
│   │       ├── staging/
│   │       └── prod/
│   └── cdk/
│       ├── app.py
│       ├── requirements.txt
│       └── stacks/
│           ├── __init__.py
│           ├── api_stack.py
│           ├── database_stack.py
│           └── pipeline_stack.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py                     # Pytest configuration
│   ├── unit/
│   │   ├── test_auth.py
│   │   ├── test_rag.py
│   │   ├── test_vector_search.py
│   │   └── test_chat.py
│   ├── integration/
│   │   ├── test_api_endpoints.py
│   │   ├── test_database.py
│   │   └── test_s3_integration.py
│   └── load/
│       └── locustfile.py               # Load testing
├── scripts/
│   ├── setup_db.py                     # Database initialization
│   ├── seed_data.py                    # Seed test data
│   ├── migrate.py                      # Run migrations
│   └── deploy.sh                       # Deployment script
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/                       # Database migrations
├── docs/
│   ├── API.md                          # API documentation
│   ├── DEPLOYMENT.md                   # Deployment guide
│   ├── ARCHITECTURE.md                 # Architecture details
│   └── CONTRIBUTING.md                 # Contribution guidelines
├── .env.example                        # Environment variables template
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml                  # Local development stack
├── Dockerfile                          # Production Docker image
├── requirements.txt                    # Python dependencies
├── requirements-dev.txt                # Development dependencies
├── pyproject.toml                      # Python project configuration
├── pytest.ini                          # Pytest configuration
├── alembic.ini                         # Alembic configuration
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- PostgreSQL 15+ (with pgvector extension)
- Redis 7+
- AWS CLI configured
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/saqirana/llm-retrieval-service.git
   cd llm-retrieval-service
   ```

2. **Set up Python virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start infrastructure services**
   ```bash
   docker-compose up -d postgres redis
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   python scripts/seed_data.py
   ```

6. **Start the development server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Access the application**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Using Docker Compose (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop all services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

## 📚 API Documentation

### Authentication

```bash
# Register a new user
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secure_password"}'

# Login and get JWT token
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secure_password"}'
```

### Document Upload

```bash
# Upload a document
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "file=@document.pdf"
```

### RAG Retrieval

```bash
# Query the RAG system
curl -X POST "http://localhost:8000/api/v1/retrieval/query" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the main topic of the documents?",
    "top_k": 5,
    "filters": {}
  }'
```

### Chat Streaming

```bash
# Stream chat responses (SSE)
curl -N -X POST "http://localhost:8000/api/v1/chat/stream" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Explain quantum computing",
    "session_id": "optional_session_id",
    "use_rag": true
  }'
```

For complete API documentation, visit the interactive docs at `/docs` after starting the server.

## 🚀 Deployment

### AWS Lambda Deployment

```bash
# Build Lambda deployment package
cd aws/lambda
docker build -t llm-retrieval-lambda .

# Deploy using AWS SAM or CDK
cd ../../infrastructure/cdk
cdk deploy ApiStack
```

### ECS/Fargate Deployment

```bash
# Build and push Docker image
docker build -t llm-retrieval-service:latest .
docker tag llm-retrieval-service:latest YOUR_ECR_REPO:latest
docker push YOUR_ECR_REPO:latest

# Deploy using Terraform
cd infrastructure/terraform/environments/prod
terraform init
terraform plan
terraform apply
```

### Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

## 🔄 CI/CD Pipeline

The project uses **GitHub Actions** for automated CI/CD:

### Continuous Integration
- Code quality checks (Black, Ruff, MyPy)
- Unit and integration tests
- Security scanning (Bandit, Safety)
- Dependency vulnerability checks
- Docker image building

### Continuous Deployment
- Automatic deployment to dev environment
- Manual approval for staging/production
- Database migration automation
- Rollback capabilities
- Smoke tests post-deployment

### Pipeline Workflow

```
Push to main → Run Tests → Build Docker Image → Deploy to Dev → 
Manual Approval → Deploy to Staging → Smoke Tests → 
Manual Approval → Deploy to Production → Notify Team
```

## 📊 Monitoring & Observability

### Metrics
- Request latency (p50, p95, p99)
- Error rates and status codes
- Token usage and costs
- Vector search performance
- Database query performance

### Logging
- Structured JSON logging
- Correlation ID tracking
- ELK Stack integration
- CloudWatch Logs

### Alerting
- PagerDuty integration
- Slack notifications
- Email alerts for critical issues
- Custom CloudWatch alarms

### Dashboards
- Grafana dashboards for real-time metrics
- CloudWatch custom dashboards
- Application performance monitoring (APM)

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test types
pytest tests/unit/
pytest tests/integration/
pytest tests/load/

# Run with specific markers
pytest -m "slow"
pytest -m "not slow"
```

## 🔐 Security

- JWT-based authentication
- Role-based access control (RBAC)
- API rate limiting
- Input validation and sanitization
- SQL injection prevention
- CORS configuration
- AWS Secrets Manager for credentials
- Encryption at rest and in transit
- Regular security audits

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards
- Follow PEP 8 style guide
- Write comprehensive tests
- Update documentation
- Use type hints
- Run pre-commit hooks

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Muhammad Saqib** - *Initial work* - [saqi_rana@hotmail.com](mailto:saqi_rana@hotmail.com)

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- LangChain for LLM orchestration
- OpenAI for GPT models
- The open-source community

## 📮 Contact

For questions or support, please reach out:
- Email: saqi_rana@hotmail.com
- GitHub Issues: [Create an issue](https://github.com/saqirana/llm-retrieval-service/issues)

---

**Built with ❤️ using modern AI/ML technologies**



