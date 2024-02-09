# Makefile
SHELL := /bin/bash

# Python tasks
lint-python:
	cd backend && flake8 .
	cd backend && black --check .

autolint-python:
	cd backend && black .

docker-build-backend:
	docker build -t flask-backend -f Dockerfile.backend .

docker-run-backend:
	docker run -p 5000:5000 flask-backend

# JavaScript tasks
lint-js:
	cd frontend && isort --check-only .
	cd frontend && npx eslint src
	cd frontend && npx prettier --check "src/**/*.{js,jsx}"

autolint-js:
	cd frontend && isort .
	cd frontend && npx eslint --fix src
	cd frontend && npx prettier --write src

docker-build-frontend:
	docker build -t flask-frontend -f Dockerfile.frontend .

docker-run-frontend:
	docker run -p 3000:3000 flask-frontend

exec-shell:
	@POD_NAME=$$(kubectl get pods -n moneybasketball --no-headers -o custom-columns=":metadata.name" | grep moneybasketball-api- | head -n 1); \
	if [ -z "$$POD_NAME" ]; then \
		echo "No pod found matching 'moneybasketball-api-<somestring>' pattern"; \
	else \
		echo "Executing shell in pod $$POD_NAME"; \
		kubectl exec -it $$POD_NAME -n moneybasketball -- /bin/sh; \
	fi

run:
	docker-compose up --build --remove-orphans

# Combined tasks
autolint: autolint-js autolint-python lint
lint: lint-python lint-js
