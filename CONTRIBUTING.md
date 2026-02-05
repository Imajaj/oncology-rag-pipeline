# Contributing to Oncology RAG Pipeline

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/Imajaj/oncology-rag-pipeline.git`
3. Create a virtual environment: `python -m venv venv`
4. Install dependencies: `pip install -r requirements.txt`
5. Install development dependencies: `pip install -r requirements-dev.txt`

## Development Workflow

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `pytest tests/`
4. Check code style: `black src/ && flake8 src/`
5. Commit: `git commit -m "feat: your feature description"`
6. Push: `git push origin feature/your-feature-name`
7. Open a Pull Request

## Code Style

- Follow PEP 8
- Use `black` for formatting
- Add type hints where possible
- Write docstrings for all functions/classes
- Keep functions focused and small (<50 lines when possible)

## Testing

- Write unit tests for new features
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage

## Documentation

- Update README.md if adding new features
- Add docstrings to new functions/classes
- Update configuration examples if needed

## Areas for Contribution

### High Priority
1. **Multi-Hop Reasoning**: Implement graph-based retrieval
2. **Table Extraction**: Add structured data extraction
3. **Fine-Tuning**: Domain-adapt retriever on medical data

### Medium Priority
4. **Additional LLM Support**: Integrate Claude, Llama-2, etc.
5. **Evaluation**: Add more test cases and metrics
6. **Performance**: Optimize latency and throughput

### Documentation
7. Improve tutorials and examples
8. Add architecture diagrams
9. Create video walkthroughs

## Commit Message Format

Use conventional commits:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding tests
- `refactor`: Code refactoring
- `perf`: Performance improvements

Example: `feat: add support for table extraction from PDFs`

## Code of Conduct

Be respectful and constructive. This is a professional, academic project.
