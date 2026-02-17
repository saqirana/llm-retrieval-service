#!/bin/bash

# Setup script for LLM Retrieval Service
# This script sets up the development environment

set -e

echo "🚀 Setting up LLM Retrieval Service..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.11"

if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]]; then
    echo -e "${RED}Error: Python $required_version or higher is required. Found: $python_version${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python version: $python_version${NC}"

# Create virtual environment
echo -e "${YELLOW}Creating virtual environment...${NC}"
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source .venv/bin/activate

# Upgrade pip
echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip > /dev/null 2>&1
echo -e "${GREEN}✓ Pip upgraded${NC}"

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install -r requirements.txt > /dev/null 2>&1
echo -e "${GREEN}✓ Production dependencies installed${NC}"

pip install -r requirements-dev.txt > /dev/null 2>&1
echo -e "${GREEN}✓ Development dependencies installed${NC}"

# Copy environment file
echo -e "${YELLOW}Setting up environment variables...${NC}"
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ .env file created from .env.example${NC}"
    echo -e "${YELLOW}⚠️  Please update .env with your API keys and configuration${NC}"
else
    echo -e "${GREEN}✓ .env file already exists${NC}"
fi

# Install pre-commit hooks
echo -e "${YELLOW}Installing pre-commit hooks...${NC}"
pre-commit install > /dev/null 2>&1
echo -e "${GREEN}✓ Pre-commit hooks installed${NC}"

# Check Docker
echo -e "${YELLOW}Checking Docker...${NC}"
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓ Docker is installed${NC}"

    # Start Docker services
    read -p "Do you want to start Docker services (PostgreSQL, Redis)? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Starting Docker services...${NC}"
        docker-compose up -d postgres redis
        echo -e "${GREEN}✓ Docker services started${NC}"
        echo -e "${YELLOW}Waiting for services to be ready...${NC}"
        sleep 5
    fi
else
    echo -e "${YELLOW}⚠️  Docker not found. Please install Docker for full functionality.${NC}"
fi

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "1. Update .env with your API keys"
echo "2. Run 'source .venv/bin/activate' to activate the virtual environment"
echo "3. Run 'uvicorn main:app --reload' to start the development server"
echo "4. Visit http://localhost:8000/docs for API documentation"
echo ""
echo "For Docker setup:"
echo "  - Start all services: docker-compose up -d"
echo "  - Stop all services: docker-compose down"
echo "  - View logs: docker-compose logs -f"
echo ""
echo "Happy coding! 🎉"

