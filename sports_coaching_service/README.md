# Sports Coaching Service

Manages sports coaching sessions, coaches, and their schedules for the sports academy.

## Features

- Coach registration and profile management
- Coaching session scheduling and tracking
- Coach availability management
- Weekly schedule management
- Session status tracking

## API Endpoints

### Coaches
#### POST /coaches/
Register a new coach with:
- name (required)
- sport_type (required: badminton/volleyball/basketball)
- experience_years (optional)
- hourly_rate (required)
- contact_number (optional)
- email (required)

#### GET /coaches/
List all coaches with filters:
- skip (optional)
- limit (optional)
- sport_type (optional filter)

#### PUT /coaches/{coach_id}/availability
Update coach availability status

### Schedules
#### POST /schedules/
Create coach schedule with:
- coach_id (required)
- day_of_week (required, 0-6)
- start_time (required, "HH:MM")
- end_time (required, "HH:MM")

#### GET /coaches/{coach_id}/schedule
Get complete schedule for a specific coach

### Sessions
#### POST /sessions/
Create a coaching session with:
- coach_id (required)
- member_id (required)
- sport_type (required)
- session_date (required)
- duration_minutes (required)
- notes (optional)

#### GET /sessions/
List all sessions with filters:
- skip (optional)
- limit (optional)
- coach_id (optional filter)
- member_id (optional filter)

#### PUT /sessions/{session_id}/status
Update session status:
- status (scheduled/completed/cancelled)

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
uvicorn app.main:app --reload --port 8003
```

## Docker Development

Build and run using Docker:
```bash
docker build -t sports-coaching-service .
docker run -p 8003:8003 sports-coaching-service
```

## API Documentation

Access the interactive API documentation at:
- Swagger UI: http://localhost:8003/docs
- ReDoc: http://localhost:8003/redoc