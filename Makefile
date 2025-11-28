# Makefile for Flask AI Application

# Variables
IMAGE_NAME = ghcr.io/andrespuglla5655/examen-recuperacion
TAG = puglla-3.0.0
CONTAINER_NAME = examen-recuperacion-app

# Default target
.PHONY: help
help:
	@echo "Flask AI Application Makefile"
	@echo "Usage:"
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run tests"
	@echo "  make run         - Run the Flask application locally"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run  - Run application in Docker container"
	@echo "  make clean       - Remove Docker container"
	@echo "  make all         - Install, test, and run locally"

# Install dependencies
.PHONY: install
install:
	pip install -r requirements.txt
	pip install pytest

# Run tests
.PHONY: test
test:
	python -m pytest tests/ -v

# Run Flask application locally
.PHONY: run
run:
	python app.py

# Build Docker image
.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME):$(TAG) -f puglla .

# Run application in Docker container
.PHONY: docker-run
docker-run:
	docker run --rm -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME):$(TAG)

# Remove Docker container
.PHONY: clean
clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Install, test, and run locally
.PHONY: all
all: install test run

# Quick development cycle
.PHONY: dev
dev: docker-build docker-run