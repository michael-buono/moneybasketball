# Makefile

# Python tasks
lint-python:
	cd backend && flake8 .
	cd backend && black --check .

autolint-python:
	cd backend && black .

docker-build-backend:
	cd backend && docker build -t flask-backend -f Dockerfile.backend .

docker-run-backend:
	cd backend && docker run -p 5000:5000 flask-backend

# JavaScript tasks
lint-js:
	cd frontend && isort --check-only .
	cd frontend && npx eslint src
	cd frontend && npx prettier --check "src/**/*.{js,jsx}"

autolint-js:
	cd frontend && isort .
	cd frontend && npx eslint --fix src
	cd frontend && npx prettier --write src

# Combined tasks
autolint: autolint-js autolint-python lint
lint: lint-python lint-js