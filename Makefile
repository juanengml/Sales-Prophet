# Variáveis
PROJECT_NAME=sales-prophet
FRONTEND_IMAGE_NAME=$(PROJECT_NAME)-frontend
BACKEND_IMAGE_NAME=$(PROJECT_NAME)-backend

# Comandos
build-frontend-image:
	docker build -t $(FRONTEND_IMAGE_NAME) -f frontend/Dockerfile .

build-backend-image:
	docker build -t $(BACKEND_IMAGE_NAME) -f backend/Dockerfile .

start-frontend:
	docker run -d --name $(FRONTEND_IMAGE_NAME) -p 8501:8501 $(FRONTEND_IMAGE_NAME)

start-backend:
	docker run -d --name $(BACKEND_IMAGE_NAME) -p 5000:5000 $(BACKEND_IMAGE_NAME)

stop-frontend:
	docker stop $(FRONTEND_IMAGE_NAME)
	docker rm $(FRONTEND_IMAGE_NAME)

stop-backend:
	docker stop $(BACKEND_IMAGE_NAME)
	docker rm $(BACKEND_IMAGE_NAME)

run:
	make build-frontend-image
	make build-backend-image
	make start-frontend
	make start-backend

stop:
	make stop-frontend
	make stop-backend

help:
	@echo "make build-frontend-image: Builds the frontend Docker image"
	@echo "make build-backend-image: Builds the backend Docker image"
	@echo "make start-frontend: Starts the frontend Docker container"
	@echo "make start-backend: Starts the backend Docker container"
	@echo "make stop-frontend: Stops the frontend Docker container"
	@echo "make stop-backend: Stops the backend Docker container"
	@echo "make run: Builds and starts both frontend and backend containers"
	@echo "make stop: Stops both frontend and backend containers"
	@echo "make help: Shows this help message"

