# Sports Academy Management System

A microservices-based system for managing a sports academy, built with FastAPI and MySQL.

## Microservices Architecture

The system consists of four microservices:

1. **Staff Service** (Port 8001)
   - Manages staff members
   - Handles staff information and specializations
   - Role-based staff management

2. **Equipment Service** (Port 8002)
   - Manages sports equipment inventory
   - Handles court bookings and maintenance
   - Tracks equipment condition and availability

3. **Gym Subscription Service** (Port 8003)
   - Manages member subscriptions
   - Handles membership types and renewals
   - Payment status tracking

4. **Sports Coaching Service** (Port 8004)
   - Manages coaching sessions
   - Handles coach schedules
   - Session booking and tracking

## Technologies Used

- FastAPI (Python web framework)
- MySQL (Database)
- SQLAlchemy (ORM)
- Docker & Docker Compose (Containerization)
- Pydantic (Data validation)

## Setup Instructions

1. **Prerequisites**
   - Docker and Docker Compose installed
   - Git installed

2. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd sports-academy-system
   ```

3. **Environment Setup**
   The docker-compose.yml file includes all necessary environment variables.

4. **Build and Run**
   ```bash
   docker-compose up --build
   ```

5. **Access Services**
   - Staff Service: http://localhost:8000/docs
   - Equipment Service: http://localhost:8001/docs
   - Gym Subscription Service: http://localhost:8002/docs
   - Sports Coaching Service: http://localhost:8003/docs

## API Documentation

Each service exposes a Swagger UI documentation at its `/docs` endpoint.

### Staff Service Endpoints
- POST /staff/ - Create new staff
- GET /staff/ - List all staff
- GET /staff/{staff_id} - Get staff details
- PUT /staff/{staff_id} - Update staff
- DELETE /staff/{staff_id} - Deactivate staff

### Equipment Service Endpoints
- POST /courts/ - Add new court
- GET /courts/ - List all courts
- PUT /courts/{court_id}/availability - Update court availability
- POST /equipment/ - Add new equipment
- GET /equipment/ - List all equipment
- PUT /equipment/{equipment_id}/quantity - Update equipment quantity

### Gym Subscription Service Endpoints
- POST /members/ - Register new member
- GET /members/ - List all members
- POST /subscriptions/ - Create subscription
- GET /subscriptions/ - List all subscriptions
- PUT /subscriptions/{subscription_id}/payment-status - Update payment status

### Sports Coaching Service Endpoints
- POST /coaches/ - Register new coach
- GET /coaches/ - List all coaches
- POST /sessions/ - Create coaching session
- GET /sessions/ - List all sessions
- PUT /sessions/{session_id}/status - Update session status
- POST /schedules/ - Create coach schedule
- GET /coaches/{coach_id}/schedule - Get coach's schedule

## Database Schema

Each service has its own MySQL database with the following main tables:

### Staff Service DB
- staff (id, name, role, specialization, contact_number, email, is_active)

### Equipment Service DB
- courts (id, name, sport_type, is_available, maintenance_status)
- equipment (id, name, sport_type, quantity, condition, unit_price)

### Gym Subscription Service DB
- members (id, name, email, phone, membership_type, is_active, joined_date)
- subscriptions (id, member_id, start_date, end_date, amount, payment_status)

### Sports Coaching Service DB
- coaches (id, name, sport_type, experience_years, hourly_rate, is_available)
- coaching_sessions (id, coach_id, member_id, sport_type, session_date, status)
- coach_schedules (id, coach_id, day_of_week, start_time, end_time)

## Error Handling

All services implement standard HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

## Development

To extend or modify the services:

1. Each service is independent and can be modified separately
2. Use the shared database utilities in the shared/ directory
3. Follow the existing pattern for new endpoints
4. Update docker-compose.yml for new services or dependencies

## Testing

Each service can be tested independently using the FastAPI test client. The Swagger UI provides an interactive way to test all endpoints.


## Service Integrations

### Integration with External Microservices

The system integrates with two external microservices developed by another team. These integrations streamline operations across employee management and vendor-related workflows via unified interfaces built in Streamlit.

---

### 1. Employee Salary Service Integration

- **Integrated With**: Staff Service  
- **Integration Point**: Combined API endpoints for employee salary management and staff registration  
- **Interface**: Streamlit application [`salary.py`](salary.py)

#### Features:
- Unified form for registering staff and employees
- Simultaneous data submission to both external and local services
- **Common Fields**:
  - `name`, `role`, `contact details`
- **Salary-Specific Fields**:
  - `employee_id`, `department_id`
- **Staff-Specific Fields**:
  - `specialization`, `years_of_experience`

#### API Endpoints:
- **Employee API**: `http://external-team-domain:3001/api/employees`  
- **Staff API**: `http://localhost:8004/staff`

---

### 2. Vendor Payment Service Integration

- **Integrated With**: Equipment Service  
- **Integration Point**: Unified equipment purchase and vendor payment processing  
- **Interface**: Streamlit application [`vendor.py`](vendor.py)

#### Features:
- Single interface for managing equipment purchases and vendor payments
- Real-time creation of purchase orders
- Automatic vendor payment initiation
- Equipment inventory auto-updates post-purchase

#### API Endpoints:
- **Vendor API**: `http://external-team-domain:3004/api/purchase-orders`  
- **Equipment API**: `http://localhost:8001/equipment`

---

### Using the Integrated Services

#### Staff-Employee Integration
```bash
streamlit run salary.py
```
- Access the unified form at: http://localhost:8501  
- Fill in both staff and employee details  
- Submit the form to create records in both systems  

#### Equipment-Vendor Integration
```bash
streamlit run vendor.py
```
- Access the purchase interface at: http://localhost:8502  
- Create purchase orders for new equipment  
- Track vendor payments and inventory updates automatically  

---

### Integration Benefits

- Streamlined data entry processes  
- Elimination of duplicate records  
- Consistent and synchronized data across systems  
- Improved operational efficiency  
- Real-time updates to both internal and external services