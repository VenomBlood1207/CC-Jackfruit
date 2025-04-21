# Equipment Management Service

Manages sports equipment inventory and court facilities for the sports academy.

## Features

- Court management and availability tracking
- Sports equipment inventory management
- Equipment maintenance status tracking
- Court maintenance scheduling

## API Endpoints

### Courts
#### POST /courts/
Create a new court with:
- name (required)
- sport_type (required: badminton/volleyball/basketball)
- maintenance_status (optional)

#### GET /courts/
List all courts with pagination support:
- skip (optional)
- limit (optional)

#### PUT /courts/{court_id}/availability
Update court availability status

### Equipment
#### POST /equipment/
Add new equipment with:
- name (required)
- sport_type (required)
- quantity (required)
- condition (optional)
- unit_price (optional)
- last_maintenance (optional)

#### GET /equipment/
List all equipment with pagination support

#### PUT /equipment/{equipment_id}/quantity
Update equipment quantity

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the service:
```bash
uvicorn app.main:app --reload --port 8001
```

## Docker Development

Build and run using Docker:
```bash
docker build -t equipment-service .
docker run -p 8001:8001 equipment-service
```

## API Documentation

Access the interactive API documentation at:
- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc