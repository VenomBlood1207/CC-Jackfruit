# Gym Subscription Service

Manages gym memberships and subscriptions for the sports academy.

## Features

- Member registration and management
- Subscription plan management
- Payment tracking
- Membership type handling (Basic/Premium/VIP)
- Automatic renewal status tracking

## API Endpoints

### Members
#### POST /members/
Register a new member with:
- name (required)
- email (required)
- phone (optional)
- membership_type (required: basic/premium/vip)

#### GET /members/
List all members with pagination support:
- skip (optional)
- limit (optional)

#### PUT /members/{member_id}
Update member information

#### DELETE /members/{member_id}
Deactivate member (soft delete)

### Subscriptions
#### POST /subscriptions/
Create a new subscription with:
- member_id (required)
- start_date (required)
- end_date (required)
- amount (required)
- renewal_status (optional)

#### GET /subscriptions/
List all subscriptions with pagination

#### PUT /subscriptions/{subscription_id}/payment-status
Update subscription payment status:
- payment_status (pending/completed/failed)

#### GET /members/{member_id}/subscriptions
Get all subscriptions for a specific member

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
uvicorn app.main:app --reload --port 8002
```

## Docker Development

Build and run using Docker:
```bash
docker build -t gym-subscription-service .
docker run -p 8002:8002 gym-subscription-service
```

## API Documentation

Access the interactive API documentation at:
- Swagger UI: http://localhost:8002/docs
- ReDoc: http://localhost:8002/redoc