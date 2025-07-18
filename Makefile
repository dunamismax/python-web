# Python Web Monorepo Makefile

.PHONY: help install clean format lint typecheck test todo weather build-todo build-weather init

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install all dependencies"
	@echo "  init         - Initialize Reflex apps"
	@echo "  todo         - Run Todo app in development mode"
	@echo "  weather      - Run Weather app in development mode"
	@echo "  build-todo   - Build Todo app for production"
	@echo "  build-weather- Build Weather app for production"
	@echo "  format       - Format code with black and isort"
	@echo "  lint         - Lint code with flake8"
	@echo "  typecheck    - Type check with mypy"
	@echo "  test         - Run tests"
	@echo "  clean        - Clean build artifacts"

# Development commands
install:
	python tools/dev.py install

init:
	python tools/dev.py init

todo:
	python tools/dev.py todo

weather:
	python tools/dev.py weather

# Build commands
build-todo:
	python tools/dev.py build-todo

build-weather:
	python tools/dev.py build-weather

# Code quality commands
format:
	python tools/dev.py format

lint:
	python tools/dev.py lint

typecheck:
	python tools/dev.py typecheck

test:
	python tools/dev.py test

# Utility commands
clean:
	python tools/dev.py clean

# Setup for new developers
setup: install init
	@echo "Setup complete! You can now run 'make todo' or 'make weather' to start development."