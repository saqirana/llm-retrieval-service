# Contributing to LLM Retrieval Service

Thank you for your interest in contributing to the LLM Retrieval Service! This document provides guidelines and instructions for contributing.

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/saqirana/llm-retrieval-service/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

### Suggesting Features

1. Check existing feature requests in Issues
2. Create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/saqirana/llm-retrieval-service.git
   cd llm-retrieval-service
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
   pre-commit install
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow PEP 8 style guide
   - Add tests for new functionality
   - Update documentation as needed

5. **Run tests and quality checks**
   ```bash
   # Run tests
   pytest
   
   # Run linters
   black .
   ruff check .
   mypy app/
   
   # Run pre-commit hooks
   pre-commit run --all-files
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

   Use conventional commit messages:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `style:` Code style changes
   - `refactor:` Code refactoring
   - `test:` Test additions or changes
   - `chore:` Maintenance tasks

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Link any related issues

## Development Guidelines

### Code Style

- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use meaningful variable and function names
- Write docstrings for all public functions

### Testing

- Write unit tests for all new functions
- Maintain >80% code coverage
- Use pytest fixtures for common setups
- Mock external dependencies

### Documentation

- Update README.md for new features
- Add docstrings to all functions
- Update API documentation
- Include examples in docstrings

### Commit Messages

Follow the conventional commits specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Example:
```
feat(auth): add OAuth2 authentication

Implement OAuth2 authentication flow with JWT tokens.
Includes token refresh and validation.

Closes #123
```

## Project Structure

```
llm-retrieval-service/
├── app/                    # Application code
│   ├── api/               # API endpoints
│   ├── core/              # Core functionality
│   ├── models/            # Database models
│   ├── schemas/           # Pydantic schemas
│   └── services/          # Business logic
├── tests/                 # Test files
├── aws/                   # AWS specific code
├── infrastructure/        # Infrastructure as code
└── docs/                  # Documentation
```

## Getting Help

- Join our [Discord community](https://discord.gg/YOUR_DISCORD)
- Ask questions in [Discussions](https://github.com/saqirana/llm-retrieval-service/discussions)
- Email: saqi_rana@hotmail.com

## Recognition

Contributors will be recognized in:
- README.md Contributors section
- Release notes
- Project documentation

Thank you for contributing! 🎉




