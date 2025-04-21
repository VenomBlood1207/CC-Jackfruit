# Staff Management Service

Handles staff information and management for the sports academy.

## Features

- Staff member registration and management
- Role-based staff categorization
- Sport specialization tracking
- Staff availability management

## API Endpoints

### POST /staff/
Create a new staff member with the following fields:
- name (required)
- role (required)
- specialization (optional)
- contact_number (optional)
- email (required)
- years_of_experience (optional)

### GET /staff/
List all staff members with pagination support:
- skip (optional): Number of records to skip
- limit (optional): Maximum number of records to return

### GET /staff/{staff_id}
Get details of a specific staff member

### PUT /staff/{staff_id}
Update staff member information

### DELETE /staff/{staff_id}
Deactivate a staff member (soft delete)

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
uvicorn app.main:app --reload --port 8000
```

## Docker Development

Build and run using Docker:
```bash
docker build -t staff-service .
docker run -p 8000:8000 staff-service
```

## API Documentation

Access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc