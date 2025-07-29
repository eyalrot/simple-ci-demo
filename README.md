# FastAPI POC - Simple CI Demo

A proof of concept FastAPI application with Docker Compose deployment.

## Features

- FastAPI with async support
- RESTful API with CRUD operations
- Pydantic models for validation
- Docker multi-stage build
- Docker Compose with Nginx reverse proxy
- Health check endpoint
- CORS middleware
- Environment configuration

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload

# Access API docs
# http://localhost:8000/docs
```

### Docker Compose Deployment

```bash
# Start the services
docker-compose up -d

# Access the application
# http://localhost (through Nginx)
# http://localhost:8000 (direct)

# Stop the services
docker-compose down
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - Swagger UI
- `GET /redoc` - ReDoc UI

### Items API
- `POST /api/v1/items/` - Create item
- `GET /api/v1/items/` - List items
- `GET /api/v1/items/{item_id}` - Get item
- `PUT /api/v1/items/{item_id}` - Update item
- `DELETE /api/v1/items/{item_id}` - Delete item

## Testing

```bash
pip install pytest httpx
pytest
```

## Environment Variables

Copy `.env.example` to `.env` and adjust values as needed.